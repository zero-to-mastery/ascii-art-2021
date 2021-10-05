# this project requires Pillow installation: https://pillow.readthedocs.io/en/stable/installation.html

# code credit goes to: https://www.hackerearth.com/practice/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
# code modified to work with Python 3 by @aneagoie

# Usage Instructions:

# 1. Clone this repo as it is!
# 2. Open Terminal/cmd prompt, change the directory to the location of this repo
<<<<<<< HEAD:community-version.py
# 3. Run the cmd 'python3 community-version.py image_file_path'
=======
# 3. Run the cmd 'python3 community_version.py -i image_file_path'
>>>>>>> 77ef4dc8712492ce9768f92235b8ef0b6526d1f0:community_version.py
# 4. Get the output on cmd window and checkout the saved text file too
# 5. To see what more the script can do with ascii, run: 'python3 community_version.py --help`

# Note:
# Please change the instructions according to the fix or features contributed code.
# comment the contribution to make others understand easy (follow the best comment practices).

<<<<<<< HEAD:community-version.py

=======
>>>>>>> 77ef4dc8712492ce9768f92235b8ef0b6526d1f0:community_version.py
import os
from PIL import Image, ImageOps  # ImageOps optional
import argparse
<<<<<<< HEAD:community-version.py
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", ".",
               '-', '_', '+', '<', '>', 'i', '!', 'l', 'I', '?',
               '/', '"', '|', '(', ')', '1', '{', '}', '[', ']',
               'r', 'c', 'v', 'u', 'n', 'x', 'z', 'j', 'f', 't',
               'L', 'C', 'J', 'U', 'Y', 'X', 'Z', 'O', '0', 'Q',
               'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm',
               '*', 'W', 'M', 'B', '8']
=======

ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
>>>>>>> 77ef4dc8712492ce9768f92235b8ef0b6526d1f0:community_version.py


def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image


def convert_to_grayscale(image):
    img = ImageOps.grayscale(image)
    return img



def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.
    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
<<<<<<< HEAD:community-version.py
    pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in
                       pixels_in_image]
=======
    pixels_to_chars = [ASCII_CHARS[int(pixel_value / range_width)]
                       for pixel_value in pixels_in_image]
>>>>>>> 77ef4dc8712492ce9768f92235b8ef0b6526d1f0:community_version.py

    return "".join(pixels_to_chars)


def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

<<<<<<< HEAD:community-version.py
    image_ascii = [pixels_to_chars[index: index + new_width] for index in
                   range(0, len_pixels_to_chars, new_width)]
=======
    image_ascii = [pixels_to_chars[index: index + new_width]
                   for index in range(0, len_pixels_to_chars, new_width)]
>>>>>>> 77ef4dc8712492ce9768f92235b8ef0b6526d1f0:community_version.py

    return "\n".join(image_ascii)


def write_to_txtfile(image_txt, out_file):
    with open(out_file, "w") as text_file:
        text_file.write(image_txt)


def handle_image_conversion(image_filepath):
    try:
        image = Image.open(image_filepath)
    except Exception as err:
        print(f"Unable to open image file {image_filepath}.")
        print(err)
    else:
        return convert_image_to_ascii(image)


def validate_file_path(path):
    if not os.path.isfile(path):
        print(f'Invalid input. Could not find file at "{path}".')
        print('A test image is located at "example/ztm-logo.png"')
        path = input('Enter a valid file path: ')
        validate_file_path(path)
    return path


def validate_file_extension(path):
    allowed_extensions = ["jpg", "jpeg", "png", "bmp", "jfif", "tiff", "gif"]
    filename, ext = os.path.splitext(path)

    if ext[1:] not in allowed_extensions:
        print(
            f"Invalid extension: {ext}. Make sure it is one of {', '.join(allowed_extensions)}.")
        path = input('Enter a valid image path: ')
        validate_file_extension(path)

    return path


<<<<<<< HEAD:community-version.py
if __name__ == '__main__':
    import sys

    parser = argparse.ArgumentParser(
        description="Converts images into ASCII art.", add_help=True)
    parser.add_argument(
        "-i", "--image", help="File path to input image", nargs=1, action="store")
    parser.add_argument(
        "-o", "--outfile", help="File path to output text file", nargs="?", action="store")

    args = parser.parse_args()

    try:
        image_file_path = args.image[0]
    except IndexError:
        image_file_path = input('Enter the image file path: ')
    image_file_path = validate_file_extension(image_file_path)

=======
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
>>>>>>> 77ef4dc8712492ce9768f92235b8ef0b6526d1f0:community_version.py
    image_file_path = validate_file_path(image_file_path)
    print(image_file_path)
    ascii_img = handle_image_conversion(image_file_path)

    if args.outfile:
        write_to_txtfile(ascii_img, args.outfile)
<<<<<<< HEAD:community-version.py
=======
    else:
        print(ascii_img)


if __name__ == '__main__':
    main()
>>>>>>> 77ef4dc8712492ce9768f92235b8ef0b6526d1f0:community_version.py
