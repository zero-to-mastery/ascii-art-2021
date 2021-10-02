# this project requires Pillow installation: https://pillow.readthedocs.io/en/stable/installation.html

#code credit goes to: https://www.hackerearth.com/practice/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
#code modified to work with Python 3 by @aneagoie
import os
from PIL import Image
ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

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

def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.
    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            range(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)

def write_to_txtfile(txt):
    with open("output.txt", "w") as text_file:
        text_file.write(txt)

def write_to_htmlfile(txt):
    with open("output.html", "w") as html_file:
        code = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>ASCII Art</title>
                <style type="text/css">
                    h2 {{
                    font-family: Arial;
                    }}
                    pre {{
                        user-select: none;
                    }}
                </style>
            </head>
            <body>
            <h2>Your Image in ASCII Code !!!</h2>
                <pre>{ascii}</pre>
            </body>
        </html>
        """.format(ascii = txt)
        html_file.write("%s" % code)
        print("\nYou can find the HTML file here: {0}\n\n".format(os.path.realpath(html_file.name)))


def handle_image_conversion(image_filepath):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception as err:
        print(f"Unable to open image file {image_filepath}.")
        print(err)
        return

    ascii_img = convert_image_to_ascii(image)
    return ascii_img
    

if __name__=='__main__':
    import sys

    try:
        image_file_path = sys.argv[1]
    except IndexError:
        image_file_path = input('Enter the image file path (an example image is located at "example/ztm-logo.png"): ')
    print(image_file_path)
    ascii_img = handle_image_conversion(image_file_path)
    print(ascii_img)
    write_to_txtfile(ascii_img)
    write_to_htmlfile(ascii_img)
