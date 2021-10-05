from PIL import Image

ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']


class ImageHandler():
    def __init__(self, image_filepath='./example/ztm-logo.png'):
        self.image_filepath = image_filepath
        self.image = self.handle_image_creation()
        self.__ascii_image = None

    def scale(self, new_width=100):
        """Resizes an image preserving the aspect ratio.
        """
        original_width, original_height = self.image.size
        aspect_ratio = original_height / float(original_width)
        new_height = int(aspect_ratio * new_width)

        return self.image.resize((new_width, new_height))

    def convert_to_grayscale(self):
        return self.image.convert('L')

    def map_pixels_to_ascii_chars(self, range_width=25):
        """Maps each pixel to an ascii char based on the range
        in which it lies.
        0-255 is divided into 11 ranges of 25 pixels each.
        """

        pixels_in_image = list(self.image.getdata())
        pixels_to_chars = [
            ASCII_CHARS[int(pixel_value / range_width)]
            for pixel_value in pixels_in_image
        ]

        return "".join(pixels_to_chars)

    def convert_image_to_ascii(self, new_width=100):
        self.image = self.scale()
        self.image = self.convert_to_grayscale()

        pixels_to_chars = self.map_pixels_to_ascii_chars()
        len_pixels_to_chars = len(pixels_to_chars)

        image_ascii = [
            pixels_to_chars[index:index + new_width]
            for index in range(0, len_pixels_to_chars, new_width)
        ]

        return "\n".join(image_ascii)

    def create_ascii_image(self):
        self.__ascii_image = self.convert_image_to_ascii()
        return self.__ascii_image

    def print_ascii_image(self):
        print(self.__ascii_image)

    def handle_image_creation(self):
        try:
            image = Image.open(self.image_filepath)
        except Exception as err:
            print(f'Unable to open image file {self.image_filepath}.', err)

        else:
            return image