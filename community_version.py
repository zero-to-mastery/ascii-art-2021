# this project requires Pillow installation: https://pillow.readthedocs.io/en/stable/installation.html

# code credit goes to: https://www.hackerearth.com/practice/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
# code modified to work with Python 3 by @aneagoie

# Usage Instructions:

# 1. Clone this repo as it is!
# 2. Open Terminal/cmd prompt, change the directory to the location of this repo
# 3. Run the cmd 'python3 community_version.py -i path/to/your_img -o path/to/file.txt -s path/to/img.png'
# 4. Get the output on cmd window and checkout the saved text file and image file too
# 5. To see what more the script can do with ascii, run: 'python3 community_version.py --help`

# Note:
# Please change the instructions according to the fix or features contributed code.
# comment the contribution to make others understand easy (follow the best comment practices).

import os
from PIL import Image, ImageDraw, ImageSequence
import argparse


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

    new_image = image.resize((new_width, new_height))
    return new_image


def convert_to_grayscale(image):
    return image.convert('L')


def map_pixels_to_ascii_chars(image, key, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.
    0-255 is divided into 11 ranges of 25 pixels each.
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


def save_gif(out_file, ascii_frames, duration):
    """Takes a list of image frames as input and combines and
    save them all in form of a gif."""
    ascii_frames[0].save(out_file, save_all=True,
                         append_images=ascii_frames[1:], loop=0, duration=duration)


def save_as_img(image_txt, out_file=None):
    """Takes the ASCII text as input, writes it to an image file and the saves
     it to the path inputted."""

    text_list = image_txt.split("\n")

    """Make a blank white image. Every row takes 10px, so height should be len(text_list) * 10 and every
     letter of a row takes 6px, so len(elements in a row) * 6 would get the
     correct width."""
    img = Image.new(
        'RGB', (len(text_list[0]) * 6, len(text_list) * 10), color='white')

    draw = ImageDraw.Draw(img)  # Creates an ImageDraw object of img.
    for i in range(len(text_list)):
        # Draws the text on the blank image.
        draw.text((0, (10 * i)), text_list[i], (0, 0, 0))

    if out_file:
        img.save(out_file)

    return img


def gif_to_ascii_frames(gif, key):
    """Extracts frames from the gif then converts them into ASCII img.
    And reutrns all the ASCII frames and the duration of the gif."""

    original_duration = gif.info["duration"]  # Get the duration of the gif.
    # Extract all the frames.
    frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]
    ascii_frames = []
    for frame in frames:
        """Convert extracted frames into ASCII frames with convert_image_to_ascii()
        and convert them into img object with the help of save_as_img()
        and append to ascii_frames."""
        ascii_frames.append(save_as_img(convert_image_to_ascii(frame, key)))

    return ascii_frames, original_duration


def handle_image_conversion(image_filepath, key_filepath, is_gif=False):
    try:
        image = Image.open(image_filepath)
    except Exception as err:
        print(f"Unable to open image file {image_filepath}.")
        print(err)
    else:
        key = key_filepath
        return (gif_to_ascii_frames(image, key) if is_gif else
                convert_image_to_ascii(image, key))


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

    return ext


def _parse_args():
    """
    Parses command-line arguments.

    The function returns an object that has the added arguments as attributes.
    To add a new argument, add another entry of 'parser.add_argument(...)'
    and specify the details you want.
    The docs for argparse are at: https://docs.python.org/3/library/argparse.html
    """
    parser = argparse.ArgumentParser(
        description="Converts images into ASCII art.")
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
    image_file_ext = validate_file_extension(args.image)
    image_file_path = validate_file_path(args.image)
    print(image_file_path)
    ascii_key_path = args.key
    print(ascii_key_path)
    ascii_img = (handle_image_conversion(image_file_path, ascii_key_path) if image_file_ext !=
                 ".gif" else handle_image_conversion(image_file_path, ascii_key_path, is_gif=True))

    if image_file_ext != ".gif":
        if args.outfile:
            write_to_txtfile(ascii_img, args.outfile)
        if args.saveimg:
            save_as_img(ascii_img, args.saveimg)
        print(ascii_img)
    else:
        if args.saveimg:
            save_gif(args.saveimg, ascii_img[0], ascii_img[1])
        if args.outfile:
            raise Exception("Can't convert gif into txt file.")


if __name__ == '__main__':
    main()
