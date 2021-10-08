# this project requires Pillow installation: https://pillow.readthedocs.io/en/stable/installation.html

# code credit goes to: https://www.hackerearth.com/practice/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
# code modified to work with Python 3 by @aneagoie

# Usage Instructions:

# 1. Clone this repo as it is!
# 2. Open Terminal/cmd prompt, change the directory to the location of this repo
# 3. Run the cmd 'python3 community_version.py -i image_file_path'
# 4. Get the output on cmd window and checkout the saved text file too
# 5. To see what more the script can do with ascii, run: 'python3 community_version.py --help`

# Note:
# Please change the instructions according to the fix or features contributed code.
# comment the contribution to make others understand easy (follow the best comment practices).
import argparse
import logging.config
import os
from PIL import Image
from logger_config import LOGGING_CONFIG

ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image


def convert_to_grayscale(image):
    return image.convert('L')


def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.
    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[int(pixel_value / range_width)]
                       for pixel_value in pixels_in_image]

    return "".join(pixels_to_chars)


def convert_image_to_ascii(image, new_width=100):
    logger.info("Converting the image to ascii")
    image = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width]
                   for index in range(0, len_pixels_to_chars, new_width)]

    logger.info("Successfully converted the image to ascii")
    return "\n".join(image_ascii)


def write_to_txtfile(image_txt, out_file):
    with open(out_file, "w") as text_file:
        text_file.write(image_txt)


def handle_image_conversion(image_filepath):
    try:
        image = Image.open(image_filepath)
    except Exception as err:
        logger.error(f"Unable to open image file {image_filepath}.")
        logger.error(err)
    else:
        return convert_image_to_ascii(image)


def validate_file_path(path):
    if not os.path.isfile(path):
        logger.error(f'Invalid input. Could not find file at "{path}".')
        logger.info('A test image is located at "example/ztm-logo.png"')
        path = input('Enter a valid file path: ')
        validate_file_path(path)
    return path


def validate_file_extension(path):
    allowed_extensions = ["jpg", "jpeg", "png", "bmp", "jfif", "tiff", "gif"]
    filename, ext = os.path.splitext(path)

    if ext[1:] not in allowed_extensions:
        logger.error(f"Invalid extension: {ext}. Make sure it is one of {', '.join(allowed_extensions)}.")
        path = input('Enter a valid image path: ')
        validate_file_extension(path)

    return path


def _parse_args():
    """
    Parses command-line arguments.

    The function returns an object that has the added arguments as attributes.
    To add a new argument, add another entry of 'parser.add_argument(...)' 
    and specify the details you want.
    The docs for argparse are at: https://docs.python.org/3/library/argparse.html
    """
    parser = argparse.ArgumentParser(description="Converts images into ASCII art.")
    parser.add_argument("-i", "--image",
                        help="File path to input image (default: %(default)s)",
                        default="./example/ztm-logo.png",
                        action="store")
    parser.add_argument("-o", "--outfile",
                        help="write the ASCII into this file instead of the default STDOUT",
                        nargs="?",
                        action="store")

    return parser.parse_args()


def main():
    args = _parse_args()
    image_file_path = validate_file_extension(args.image)
    image_file_path = validate_file_path(image_file_path)
    logger.info(image_file_path)
    ascii_img = handle_image_conversion(image_file_path)

    if args.outfile:
        write_to_txtfile(ascii_img, args.outfile)
    else:
        print(ascii_img)


if __name__ == '__main__':
    main()
