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

    def __init__(self,
                 input_video_path,
                 output_video_dir=None,
                 use_hevc=False):
        self.media_file_info = None
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.ffmpeg_path = os.path.join(self.current_dir, 'bin', 'ffmpeg.exe')
        self.cmd_args = {
            "ffmpeg_path": self.ffmpeg_path,
            "OUTPUT_FLAG": "-i",
            "input_path": None,
            "V_MAP_FLAG": "-map",
            "video_map_option": "0:v",
            "A_MAP_FLAG": "-map",
            "audio_map_option": "0:a",
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
        print(_input_video_path, output_video_path)
        self.cmd_args["input_path"] = _input_video_path
        self.cmd_args["output_path"] = output_video_path
        self.media_file_info: MediaFileInfo = MediaFileInfo(_input_video_path)

    def modify_adaptive_args(self, _qos):
        """
        Modify adaptive compressor args (e.g. `resolution`, `bitrate`, etc.)
        """
        # calculate aspect ratio -> output resolution
        act_ratio = self.media_file_info.width / self.media_file_info.height
        COMMON_RATIO = [9 / 16, 3 / 4, 1, 4 / 3, 16 / 9, 21 / 9]
        if act_ratio >= 1:
            QOS_MAP = {
                0: (int(min(360, self.media_file_info.height)), "30"),
                1: (int(min(480, self.media_file_info.height)), "30"),
                2: (int(min(720, self.media_file_info.height)), "60")
            }
            act_h = QOS_MAP[_qos][0]
            act_w = int(act_h * act_ratio)
        else:
            QOS_MAP = {
                0: (int(min(360, self.media_file_info.width)), "30"),
                1: (int(min(480, self.media_file_info.width)), "30"),
                2: (int(min(720, self.media_file_info.width)), "60")
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
        # calculate optimized video bit rate
        opt_bitrate = min(max(self.media_file_info.bitrate // 2, 200_000),
                          (act_w * act_h * 1.5 * (_qos + 2)))
        if self.use_hevc:
            opt_bitrate = opt_bitrate * 0.65
        self.cmd_args["video_output_bitrate"] = f"{opt_bitrate}"

    def run(self, qos: Literal[0, 1, 2] = 0):
        self.modify_adaptive_args(qos)
        # Check stream existence and property
        has_video_stream: bool = self.media_file_info.has_video_stream
        has_audio_stream: bool = self.media_file_info.has_audio_stream
        total_duration = self.media_file_info.total_duration
        # delete args if relevant stream not exist
        if has_video_stream and has_audio_stream:
            cmd_args = [val for val in self.cmd_args.values()]
        elif not has_audio_stream and has_video_stream:
            cmd_args = [
                val for key, val in self.cmd_args.items()
                if not ("A_" in key or "audio_" in key)
            ]
        elif not has_video_stream and has_audio_stream:
            cmd_args = [
                val for key, val in self.cmd_args.items()
                if not ("V_" in key or "video_" in key)
            ]
        else:
            raise RuntimeError("No stream detected in file.")

        # Run script in a terminal instance
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
                if "Lsize=" in line:
                    print(100)
                    time.sleep(3)
                    res.terminate()
                    break
                # calculate progress bar value
                if "time=" in line:
                    pattern = re.compile(r"time=(\d+):(\d+):(\d+).(\d+)")
                    try:
                        l_time = [float(d) for d in pattern.findall(line)[0]]
                    except IndexError:
                        if "time=N/A" in line:
                            continue
                    f_time = l_time[0] * 3600 + l_time[1] * 60 + l_time[2]
                    print(f"{f_time * 100 / total_duration:.0f}")
