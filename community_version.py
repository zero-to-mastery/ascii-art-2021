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

import os
from PIL import Image, ImageDraw
import argparse

# ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
# ASCII_CHARS = [ '#', '@', '$', '0', '+', '?', '!', '=', '&', ';', '-', '*', ':', '~', ',', '.']

ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png", "bmp", "jfif", "tiff", "gif"]

def get_ascii_key(akey_filepath):
    """Pull a specific keyfile to index for ASCII rendering
    """
    with open(akey_filepath) as keyfile:
        return list(keyfile.read().strip())


def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))


def convert_to_grayscale(image):
    return image.convert('L')


def map_pixels_to_ascii_chars(image, key, range_width=16):
    """Maps each pixel to an ascii char based on the range
    in which it lies.
    0-255 is divided into 16 ranges of 16 pixels each.
    """
    ascii_key = get_ascii_key(key)
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ascii_key[int(pixel_value / range_width)]
                       for pixel_value in pixels_in_image]

    return "".join(pixels_to_chars)


def convert_image_to_ascii(image, key, new_width=100):
    image = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image, key)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width]
                   for index in range(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)


def write_to_txtfile(image_txt, out_file):
    with open(out_file, "w") as text_file:
        text_file.write(image_txt)


def save_as_img(image_txt, out_file):
    """Takes the ASCII text as input, writes it to an image file and the saves
     it to the path inputted."""

    # Make a blank white image.
    text_list = image_txt.split("\n")

    """Every row takes 10px, so height should be len(text_list) * 10 and every
     letter of a row takes 6px, so len(elements in a row) * 6 would get the
     correct width."""
    img = Image.new(
        'RGB', (len(text_list[0]) * 6, len(text_list) * 10), color='white')

    draw = ImageDraw.Draw(img)  # Creates an ImageDraw object of img.
    for i in range(len(text_list)):
        # Draws the text on the blank image.
        draw.text((0, (10 * i)), text_list[i], (0, 0, 0))

    img.save(out_file)


def handle_image_conversion(image_filepath, key_filepath):
    try:
        image = Image.open(image_filepath)
    except Exception as err:
        print(f"Unable to open image file {image_filepath}.")
        print(err)
    else:
        return convert_image_to_ascii(image, key_filepath)


def validate_file_path(path):
    if not os.path.isfile(path):
        print(f'Invalid input. Could not find file at "{path}".')
        print('A test image is located at "example/ztm-logo.png"')
        path = input('Enter a valid file path: ')
        validate_file_path(path)
    return path


def is_supported(path: str) -> bool:
    """
    Checks if the given path is for a supported file.
    It uses the file extension in the path and compares
    it against ALLOWED_EXTENSIONS.
    """
    _, ext = os.path.splitext(path)
    return ext[1:].lower() in set(ALLOWED_EXTENSIONS)


def validate_file_extension(path):
    if not is_supported(path):
        print(f"File not supported. Make sure it is one of {', '.join(ALLOWED_EXTENSIONS)}.")
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
    parser.add_argument("-k", "--key",
                        help="Key of ASCII characters to use in rendering",
                        default="./akey.txt",
                        action="store")
    parser.add_argument("-s", "--saveimg",
                        help="Save the ASCII into an image file",
                        nargs="?",
                        action="store")

    return parser.parse_args()


def main():
    args = _parse_args()
    image_file_path = validate_file_extension(args.image)
    image_file_path = validate_file_path(image_file_path)
    print(image_file_path)
    ascii_key_path = args.key
    print(ascii_key_path)
    ascii_img = handle_image_conversion(image_file_path, ascii_key_path)
    if args.outfile:
        write_to_txtfile(ascii_img, args.outfile)
    if args.saveimg:
        save_as_img(ascii_img, args.saveimg)
    else:
        print(ascii_img)


if __name__ == '__main__':
    main()
