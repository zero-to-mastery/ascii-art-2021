from modules import file_manager
from modules import command_line_args as cli

from modules.image_handler import ImageHandler


def main():
    args = cli.parse_args()

    image_file_path = file_manager.validate_file_extension(args.image)
    image_file_path = file_manager.validate_file_path(image_file_path)

    ztm_logo_img_handler = ImageHandler(image_file_path)

    ascii_img = ztm_logo_img_handler.create_ascii_image()
    ztm_logo_img_handler.print_ascii_image()

    if args.outfile:
        file_manager.write_to_file(ascii_img, args.outfile)
    else:
        ztm_logo_img_handler.print_ascii_image()


if __name__ == "__main__":
    main()
