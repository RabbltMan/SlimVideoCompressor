import os


class Compressor:
    def __init__(self, input_video_path: str, output_video_dir: str):
        """
        :param input_video_path: original video file
        :param output_video_dir: directory for compressed video output
        """
        self.input_video_path = input_video_path
        filename, _ = os.path.splitext(os.path.basename(self.input_video_path))
        self.output_video_path = output_video_dir + f"{filename}"

    def run(self):
        pass


if __name__ == "__main__":
    Compressor("example.mp4", "./")
