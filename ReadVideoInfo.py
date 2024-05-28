import os
import subprocess


class MediaFileInfo:

    def __init__(self, input_file_path: str):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.ffmpeg_path = os.path.join(self.current_dir, 'bin', 'ffmpeg.exe')
        self.ffprobe_path = os.path.join(self.current_dir, 'bin', 'ffprobe.exe')
        self.input_path = input_file_path
        self.get_stream_info()

    def get_stream_info(self):
        res = subprocess.run(
            args=[self.ffprobe_path, '-i', self.input_path, "-show_streams"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True)
        print(res.stdout)


MediaFileInfo("example.mp4")
