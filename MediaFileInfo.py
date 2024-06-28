import os
import subprocess


class MediaFileInfo:
    """
    A class retrieves information from the input media file using ffprobe.
    """

    def __init__(self, input_file_path: str):
        # String-type stream keywords
        self.S_STREAM_KEYWORDS = (
            "codec_name",
            "codec_type",
        )
        # Float-type stream keywords
        self.F_STREAM_KEYWORDS = ("width", "height", "start_time", "duration",
                                  "bit_rate", "r_frame_rate", "sample_rate")
        self.current_dir = os.path.abspath("./")
        self.ffprobe_path = os.path.join(self.current_dir, "bin",
                                         "ffprobe.exe")
        if not os.path.exists(self.ffprobe_path):
            raise DependencyNotFoundError("ffprobe.exe Not Found")
        
        self.input_path = input_file_path
        self.width = 0.0
        self.height = 1e-5
        self.total_duration = 0.0
        self.bitrate = 0
        self.has_audio_stream = False
        self.has_video_stream = False
        self.streams = self.get_stream_info()

    def get_stream_info(self):
        # Get stream info via ffprobe
        res = subprocess.run(
            args=[self.ffprobe_path, '-i', self.input_path, "-show_streams"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True)
        streams = []
        stream_info = res.stdout.split('\n')
        try:
            assert (stream_info[0] == "[STREAM]"
                    and stream_info[-2] == "[/STREAM]")
        except AssertionError:
            raise UnsupportedInputError("Unsupported Input File")

        # Stream info parser
        for line in stream_info:
            # upcoming new stream
            if "[STREAM]" in line:
                streams.append(dict())
                continue
            # get stream attributes at stream end tag
            if "[/STREAM]" in line:
                # Calculate duration
                self.total_duration = max(
                    self.total_duration,
                    streams[-1]["start_time"] + streams[-1]["duration"])
                if streams[-1]["codec_type"] == "video":
                    self.has_video_stream = True
                    self.width = max(streams[-1]["width"], self.width)
                    self.height = max(streams[-1]["height"], self.height)
                    self.bitrate = max(streams[-1]["bit_rate"], self.bitrate)
                elif streams[-1]["codec_type"] == "audio":
                    self.has_audio_stream = True

            # properties of current stream
            if "=" in line:
                item, val = line.split("=")
                if item in self.S_STREAM_KEYWORDS:
                    streams[-1][item] = val
                elif item in self.F_STREAM_KEYWORDS:
                    if "/" in val:
                        val = [float(f) for f in val.split("/")]
                        assert (len(val) == 2)
                        if val[1] == 0:
                            continue
                        else:
                            val = val[0] / val[1]
                    else:
                        val = float(val)
                    streams[-1][item] = val
        return streams


class UnsupportedInputError(Exception):
    ...


class DependencyNotFoundError(Exception):
    ...
