import argparse
import logging
import os
import platform
import time
import traceback

import MediaFileInfo
import Compressor


def parse_arguments():
    parser = argparse.ArgumentParser(description='Slim Video Compressor')

    parser.add_argument("-i",
                        '--input_file_path',
                        required=True,
                        type=str,
                        help='Input file path')
    parser.add_argument("-o",
                        '--output_file_dir',
                        required=True,
                        type=str,
                        default=None,
                        help='Output file directory')
    parser.add_argument('--use_hevc',
                        action='store_true',
                        help='Use HEVC codec')
    parser.add_argument('--qos',
                        type=int,
                        choices=[0, 1, 2],
                        default=1,
                        help='Output file quality, 0 to 2, default 1')

    _args = parser.parse_args()
    return _args


log_dir = os.path.abspath("./logs/")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s |%(levelname)s| %(module)s:%(lineno)d > %(message)s",
    filename=os.path.join(log_dir, f"log_{int(time.time())}.log"),
    filemode="w")
logger = logging.getLogger("compressor_app")
system_info = f"Running on: {platform.system()} Version {platform.version()}"
logger.info(system_info)

args = parse_arguments()
i_file_path = os.path.abspath(args.input_file_path)
o_file_dir = os.path.abspath(args.output_file_dir)
use_hevc = args.use_hevc
qos = args.qos

try:
    Compressor.Compressor(i_file_path, o_file_dir, use_hevc, logger).run(qos)

except AssertionError:
    logger.error("There's something wrong with ffmpeg...")
    print("ERROR:FFPROBE_RUNTIME")
    logger.error(traceback.format_exc())

except MediaFileInfo.UnsupportedInputError:
    logger.error("Cannot compress selected input file!")
    print("ERROR:UNSUPPORT_INPUT")
    logger.error(traceback.format_exc())

except MediaFileInfo.DependencyNotFoundError:
    logger.error("Dependency ffprobe.exe not found!")
    print("ERROR:FFPROBE_NOT_EXIST")
    logger.error(traceback.format_exc())

except Compressor.DependencyNotFoundError:
    logger.error("Dependency ffmpeg.exe nod found!")
    print("ERROR:FFMPEG_NOT_EXIST")
    logger.error(traceback.format_exc())

except Compressor.NoStreamError:
    logger.error("No stream detected in input file!")
    print("ERROR:NO_STREAM")
    logger.error(traceback.format_exc())

except Exception:
    logger.error("An uncommon exception occurred.")
    print("ERROR:OTHERS")
    logger.error(traceback.format_exc())
