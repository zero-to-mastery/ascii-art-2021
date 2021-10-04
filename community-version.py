# this project requires Pillow installation: https://pillow.readthedocs.io/en/stable/installation.html

# code credit goes to: https://www.hackerearth.com/practice/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
# code modified to work with Python 3 by @aneagoie

# Usage Instructions:

# 1. Clone this repo as it is!
# 2. Open Terminal/cmd prompt, change the directory to the location of this repo
# 3. Run the cmd 'python3 community-version.py image_file_path' 
# 4. Get the output on cmd window and checkout the saved text file too

# Note:
# Please change the instructions according to the fix or features contributed code. 
# comment the contribution to make others understand easy (follow the best comment practices).

import argparse
import sys
import os

from image_handler import ImageHandler


def write_to_txtfile(image_txt, out_file):
    with open(out_file, "w") as text_file:
        text_file.write(image_txt)


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
        print(f"Invalid extension: {ext}. Make sure it is one of {', '.join(allowed_extensions)}.")
        path = input('Enter a valid image path: ')
        validate_file_extension(path)

    return path

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Converts images into ASCII art.", add_help=True)
    parser.add_argument("-i", "--image", help="File path to input image", nargs=1, action="store")
    parser.add_argument("-o", "--outfile", help="File path to output text file", nargs="?", action="store")

    args = parser.parse_args()

    try:
        image_file_path = args.image[0]
    except IndexError:
        image_file_path = input('Enter the image file path: ')
        
    image_file_path = validate_file_extension(image_file_path)
    image_file_path = validate_file_path(image_file_path)
    
    ztm_logo_img_handler = ImageHandler(image_file_path)
    
    print(image_file_path)
    ascii_img = ztm_logo_img_handler.create_ascii_image()
    
    print(ascii_img)

    if args.outfile is not None:
        write_to_txtfile(ascii_img, args.outfile)

