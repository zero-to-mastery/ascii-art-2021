import argparse


def parse_args():
    """
    Parses command-line arguments.

    The function returns an object that has the added arguments as attributes.
    To add a new argument, add another entry of 'parser.add_argument(...)'
    and specify the details you want.
    The docs for argparse are at: https://docs.python.org/3/library/argparse.html
    """
    parser = argparse.ArgumentParser(
        description="Converts images into ASCII art.")
    parser.add_argument("-i",
                        "--image",
                        help="File path to input image (default: %(default)s)",
                        default="./example/ztm-logo.png",
                        action="store")
    parser.add_argument(
        "-o",
        "--outfile",
        help="write the ASCII into this file instead of the default STDOUT",
        nargs="?",
        action="store")

    return parser.parse_args()