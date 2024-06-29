import logging
import os
import random
import re
import string
import subprocess
import time
from typing import Literal

from MediaFileInfo import MediaFileInfo


def gen_suffix():
    suffix = f"{int(time.time())}"[-2:]
    suffix += ''.join(random.choices(string.ascii_letters, k=2))
    suffix = [*suffix]
    random.shuffle(suffix)
    suffix = "".join(suffix)
    return suffix


class Compressor:

    def __init__(self, input_video_path, output_video_dir, use_hevc: bool,
                 logger: logging.Logger):
        self.logger = logger
        self.media_file_info = None
        self.current_dir = os.path.abspath("./")
        self.ffmpeg_path = os.path.join(self.current_dir, 'bin', 'ffmpeg.exe')
        if not os.path.exists(self.ffmpeg_path):
            raise DependencyNotFoundError("ffmpeg.exe Not Found")

        self.cmd_args = {
            "ffmpeg_path": self.ffmpeg_path,
            "OUTPUT_FLAG": "-i",
            "input_path": None,
            "A_MERGE_FLAG": "-filter_complex",
            "audio_merge_option": '"[0:1][0:2] amerge=inputs=2"',
            "V_MAP_FLAG": "-map",
            "video_map_option": "0:v",
            # "A_MAP_FLAG": "-map",
            # "audio_map_option": "[aout]",
            "V_CODEC_FLAG": "-vcodec",
            "video_codec": "libx264",
            "V_RES_FLAG": "-s",
            "video_output_res": '320x180',
            "V_FPS_FLAG": "-r",
            "video_output_fps": "30",
            "V_BITRATE_FLAG": "-b:v",
            "video_output_bitrate": "300k",
            "A_CODEC_FLAG": "-acodec",
            "audio_codec": "aac",
            "A_BITRATE_FLAG": "-b:a",
            "audio_output_bitrate": "48k",
            "output_path": None
        }
        # Apply HEVC Encoder for output video
        self.use_hevc = use_hevc
        if self.use_hevc:
            self.cmd_args["video_codec"] = "libx265"
            self.logger.info("Encoder libx265 encoder enabled.")

        self.update_path(input_video_path, output_video_dir)

    def update_path(self, _input_video_path, _output_video_dir):
        """
        Update path arguments
        :param _input_video_path: original video file
        :param _output_video_dir: directory for compressed video output
        """
        assert _input_video_path is not None
        default_output_dir = os.path.dirname(_input_video_path)
        filename, _ = os.path.splitext(os.path.basename(_input_video_path))
        if _output_video_dir is None:
            output_video_path = default_output_dir + "\\" + f"{filename}_{gen_suffix()}.mp4"
        else:
            output_video_path = _output_video_dir + "\\" + f"{filename}_{gen_suffix()}.mp4"
        self.cmd_args["input_path"] = _input_video_path
        self.logger.info(f"Updated input path: {_input_video_path}")
        self.cmd_args["output_path"] = output_video_path
        self.logger.info(f"Updated input path: {output_video_path}")
        self.media_file_info = MediaFileInfo(_input_video_path, self.logger)

    def modify_adaptive_args(self, _qos):
        """
        Modify adaptive compressor args (e.g. `resolution`, `bitrate`, etc.)
        """
        # calculate aspect ratio -> output resolution
        act_ratio = self.media_file_info.width / self.media_file_info.height
        COMMON_RATIO = [9 / 16, 3 / 4, 1, 4 / 3, 16 / 9, 21 / 9]

        if act_ratio >= 1:
            QOS_MAP = {
                0: (int(min(360, self.media_file_info.height)), "30", "48k"),
                1: (int(min(480, self.media_file_info.height)), "45", "64k"),
                2: (int(min(640, self.media_file_info.height)), "60", "96k")
            }
            act_h = QOS_MAP[_qos][0]
            act_w = int(act_h * act_ratio)
        else:
            QOS_MAP = {
                0: (int(min(360, self.media_file_info.width)), "30", "48k"),
                1: (int(min(480, self.media_file_info.width)), "45", "64k"),
                2: (int(min(640, self.media_file_info.width)), "60", "96k")
            }
            act_w = QOS_MAP[_qos][0]
            act_h = int(act_w / act_ratio)

        _, act_ratio = sorted([(abs(act_ratio - r), r)
                               for r in COMMON_RATIO])[0]
        if act_w % 2 != 0:
            act_w += 1
        if act_h % 2 != 0:
            act_h += 1

        self.cmd_args["video_output_res"] = f"{act_w}x{act_h}"
        self.cmd_args["video_output_fps"] = QOS_MAP[_qos][1]
        self.cmd_args["audio_output_bitrate"] = QOS_MAP[_qos][2]
        self.logger.info(
            f"Adjusted video output args: {QOS_MAP[_qos][1]}fps@{act_w}x{act_h}"
        )

        # calculate optimized video bit rate
        opt_bitrate = min(max(self.media_file_info.bitrate // 2, 200_000),
                          (act_w * act_h * 1.7 * (_qos + 2)))
        if self.use_hevc:
            opt_bitrate = opt_bitrate * 0.55
        self.logger.info(f"output video bit rate = {opt_bitrate}")
        self.cmd_args["video_output_bitrate"] = f"{opt_bitrate}"

    def run(self, qos: Literal[0, 1, 2] = 0):
        self.modify_adaptive_args(qos)

        # Check stream existence and property
        has_video_stream: bool = self.media_file_info.has_video_stream
        has_audio_stream: bool = self.media_file_info.has_audio_stream
        total_duration = self.media_file_info.total_duration
        audio_stream_count = self.media_file_info.audio_stream_count

        # delete args if relevant stream not exist
        if has_video_stream and has_audio_stream:
            self.logger.info("Video and audio stream detected!")
            amerge_arg = f" amerge=inputs={audio_stream_count}"
            for i in range(audio_stream_count, 0, -1):
                amerge_arg = f"[0:{i}]" + amerge_arg
            self.cmd_args["audio_merge_option"] = amerge_arg
            cmd_args = [val for val in self.cmd_args.values()]
            self.logger.info(
                f"FFmpeg command generated:\n\t{'\n\t'.join(cmd_args)}")
        elif not has_audio_stream and has_video_stream:
            self.logger.warn(
                "Video stream detected but no audio stream detected!")
            cmd_args = [
                val for key, val in self.cmd_args.items()
                if not ("A_" in key or "audio_" in key)
            ]
            self.logger.info(
                f"FFmpeg command generated:\n\t{'\n\t'.join(cmd_args)}")
        elif not has_video_stream and has_audio_stream:
            self.logger.warn(
                "Audio stream detected but no video stream detected!")
            amerge_arg = f" amerge=inputs={audio_stream_count}"
            for i in range(audio_stream_count, 0, -1):
                amerge_arg = f"[0:{i}]" + amerge_arg
            self.cmd_args["audio_merge_option"] = amerge_arg
            cmd_args = [
                val for key, val in self.cmd_args.items()
                if not ("V_" in key or "video_" in key)
            ]
            self.logger.info(
                f"FFmpeg command generated:\n\t{'\n\t'.join(cmd_args)}")
        else:
            raise NoStreamError("No stream detected in file.")

        # Merge audio streams if there are multiple ones

        # Run script in a terminal instance
        self.logger.info("Starting FFmpeg subprocess...")
        timer = int(time.time())
        res = subprocess.Popen(args=cmd_args,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               shell=True,
                               universal_newlines=True)

        while True:
            # Read ffmpeg output info in stderr
            line = res.stderr.readline()
            if line:
                # `Lsize=` occur when compression process done
                # print(line[:-1])
                if "Lsize=" in line:
                    self.logger.info(
                        f"Captured info from FFmpeg output:\n\t{line[:-1]}")
                    MediaFileInfo(self.cmd_args["output_path"], self.logger)
                    time.sleep(1.5)
                    print("PROGRESS:100")
                    res.terminate()
                    timer = int(time.time() - timer)
                    self.logger.info(
                        f"Done in {timer}s! FFmpeg subprocess terminated!")
                    break

                # calculate progress bar value
                if "time=" in line:
                    pattern = re.compile(r"time=(\d+):(\d+):(\d+).(\d+)")
                    try:
                        l_time = [float(d) for d in pattern.findall(line)[0]]
                    except IndexError:
                        if "time=N/A" in line:
                            self.logger.warn(
                                f"Cannot capture current media file timestamp!\n{line}"
                            )
                            continue
                    f_time = l_time[0] * 3600 + l_time[1] * 60 + l_time[2]
                    print(f"PROGRESS:{f_time * 100 / total_duration:.0f}")


class DependencyNotFoundError(Exception):
    ...


class NoStreamError(Exception):
    ...
