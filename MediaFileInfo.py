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
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.ffprobe_path = os.path.join(self.current_dir, 'bin',
                                         'ffprobe.exe')
        self.input_path = input_file_path
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

        assert (stream_info[0] == "[STREAM]"
                and stream_info[-2] == "[/STREAM]")
        # Stream info parser
        for line in stream_info:
            # upcoming new stream
            if "[STREAM]" in line:
                streams.append(dict())
                continue
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
