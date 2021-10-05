import os

FILE_EXTENSIONS = ("jpg", "jpeg", "png", "bmp", "jfif", "tiff", "gif")


def write_to_file(image, output_file):
    with open(output_file, "w") as text_file:
        text_file.write(image)


def validate_file_path(path):
    if not os.path.isfile(path):
        print(f'Invalid input. Could not find file at "{path}".')
        print('A test image is located at "example/ztm-logo.png"')

        path = input('Enter a valid file path: ')
        validate_file_path(path)

    return path


def validate_file_extension(path):

    filename, ext = os.path.splitext(path)

    if ext[1:] not in FILE_EXTENSIONS:
        print(
            f"Invalid extension: {ext}. Make sure it is one of {', '.join(FILE_EXTENSIONS)}."
        )
        path = input('Enter a valid image path: ')
        validate_file_extension(path)

    return path