import os
import re
import subprocess
from time import sleep

from MediaFileInfo import MediaFileInfo


class Compressor:

    def __init__(self):
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

    def modify_adaptive_args(self, media_file_info):
        """
        Modify adaptive compressor args (e.g. `resolution`, `bitrate`, etc.)
        """
        pass

    def run(self, input_video_path, output_video_dir=None):
        """
        :param input_video_path: original video file
        :param output_video_dir: directory for compressed video output
        """
        assert input_video_path is not None
        default_output_dir = os.path.dirname(input_video_path)
        filename, _ = os.path.splitext(os.path.basename(input_video_path))

        if output_video_dir is None:
            output_video_path = default_output_dir + f"{filename}_.mp4"
        else:
            output_video_path = output_video_dir + f"{filename}_.mp4"

        self.cmd_args["input_path"] = input_video_path
        self.cmd_args["output_path"] = output_video_path

        media_file_info = MediaFileInfo(input_video_path)
        self.modify_adaptive_args(media_file_info)

        # Check stream existence and property
        has_video_stream: bool = False
        has_audio_stream: bool = False
        total_duration = 0.0

        for stream in media_file_info.streams:
            # check stream existence
            if stream["codec_type"] == "video":
                has_video_stream = True
            elif stream["codec_type"] == "audio":
                has_audio_stream = True
            # calculate media file duration
            total_duration = max(total_duration,
                                 stream["start_time"] + stream["duration"])

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
                # print(line, end='')
                # `Lsize=` occur when compression process done
                if "Lsize=" in line:
                    sleep(5)
                    res.terminate()
                    print("100")
                    break
                # calculate progress bar value
                if "time=" in line:
                    pattern = re.compile(r"time=(\d+):(\d+):(\d+).(\d+)")
                    l_time = [float(d) for d in pattern.findall(line)[0]]
                    f_time = l_time[0] * 3600 + l_time[1] * 60 + l_time[2]
                    print(f"{f_time * 100 / total_duration:.0f}")


if __name__ == "__main__":
    Compressor().run("example2.mp4")
