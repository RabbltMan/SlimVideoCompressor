import os
import subprocess

from MediaFileInfo import MediaFileInfo


class Compressor:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.ffmpeg_path = os.path.join(self.current_dir, 'bin', 'ffmpeg.exe')
        self.output_video_codec = ""
        self.output_audio_codec = ""
        self.output_video_bitrate = 500_000

    def run(self, input_video_path, output_video_dir):
        """
        :param input_video_path: original video file
        :param output_video_dir: directory for compressed video output
        """
        filename, _ = os.path.splitext(os.path.basename(input_video_path))
        output_video_path = output_video_dir + f"{filename}_.mp4"
        for stream in MediaFileInfo(input_video_path).streams:
            if stream["codec_type"] == "video":
                pass
            elif stream["codec_type"] == "audio":
                pass
        res = subprocess.run(
            args=[self.ffmpeg_path, '-i', input_video_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True)


if __name__ == "__main__":
    Compressor()
