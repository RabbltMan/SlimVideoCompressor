import argparse
import os

from Compressor import Compressor


def parse_arguments():
    parser = argparse.ArgumentParser(description='Slim Video Compressor')

    parser.add_argument("-i",
                        '--input_file_path',
                        required=True,
                        type=str,
                        help='Input file path')
    parser.add_argument("-o",
                        '--output_file_dir',
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


if __name__ == '__main__':
    args = parse_arguments()
    i_file_path = os.path.abspath(args.input_file_path)
    o_file_dir = os.path.abspath(args.output_file_dir)
    use_hevc = args.use_hevc
    qos = args.qos
    Compressor(i_file_path, o_file_dir, use_hevc).run(qos)
