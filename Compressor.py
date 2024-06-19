import os
import subprocess

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
        has_video_stream: bool = False
        has_audio_stream: bool = False
        for stream in MediaFileInfo(input_video_path).streams:
            if stream["codec_type"] == "video":
                has_video_stream = True
            elif stream["codec_type"] == "audio":
                has_audio_stream = True

        if has_video_stream and has_audio_stream:
            cmd_args = [val for val in self.cmd_args.values()]
        elif not has_video_stream and has_audio_stream:
            cmd_args = [val for key, val in self.cmd_args.items() if not ("V_" in key or "video_" in key)]
        elif not has_audio_stream and has_video_stream:
            cmd_args = [val for key, val in self.cmd_args.items() if not ("A_" in key or "audio_" in key)]
        else:
            raise RuntimeError("No video or audio stream detected in input file.")
        res = subprocess.run(args=cmd_args,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             universal_newlines=True)
        print(res.stdout)
        print(res.stderr)


if __name__ == "__main__":
    Compressor().run("example.mp4")
