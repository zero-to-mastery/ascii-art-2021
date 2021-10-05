"""
This module uses tkinter.
For installation instructions, see https://tkdocs.com/tutorial/install.html
"""
from tkinter import *
import sys

from community_version import write_to_txtfile, handle_image_conversion


def main():
    global entry1
    try:
        image_file_path = sys.argv[1]
    except IndexError:
        image_file_path = entry1.get()
    ascii_img = handle_image_conversion(image_file_path)
    print(ascii_img)
    write_to_txtfile(ascii_img, "output.txt")


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x220")
    root.title("Image to ASCII converter")
    root.configure(background="black")
    root.resizable(0, 0)

    Label(root, text="Image to ASCII Convertor", fg="black", font=("Times", 25, "bold"), width=25).pack()

    label1 = Label(root, text="Please enter file path - ", fg="black", font=(15))
    label1.place(x=80, y=60)

    entry1 = Entry(root, bd=5, font=(15), width=70)
    entry1.bind(main)
    entry1.place(x=80, y=100)

    button1 = Button(root, text="Convert", font=("Times", 20), width=10, padx=5, pady=5, command=main)
    button1.place(x=310, y=150)

    root.mainloop()
