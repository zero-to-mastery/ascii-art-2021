"""
This module uses tkinter.
For installation instructions, see https://tkdocs.com/tutorial/install.html
"""
import tkinter as tk
from tkinter import filedialog, Label, Entry, Button
import sys

from community_version import handle_image_conversion, ALLOWED_EXTENSIONS

# todo: Add keyfile selection through app
KEYFILE = './akey.txt'
FILE_TYPES = [(f'{ext.upper()} Files', f'*.{ext}') for ext in ALLOWED_EXTENSIONS] + [('All Files', '*.*')]


def browse_pic(parent):
    """
    Allows user to browse directories for file and provides path to entry1
    """
    global path_entry
    tempdir = filedialog.askopenfilename(parent=parent,
                                         filetypes=FILE_TYPES,
                                         title='Please select a file')
    path_entry.delete(0, last=tk.END)
    path_entry.insert(tk.END, tempdir)


def main():
    global path_entry
    try:
        image_file_path = sys.argv[1]
    except IndexError:
        image_file_path = path_entry.get()

    if not image_file_path:
        print('Image not selected.')
        return

    if ascii_img := handle_image_conversion(image_file_path, KEYFILE):
        print(ascii_img)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("900x500")
    root.title("Image to ASCII converter")
    root.configure(background="black")
    root.resizable(0, 0)

    Label(root, text="Image to ASCII Converter", fg="black", font=("Times", 25, "bold"),
          width=25, pady=5, padx=25).pack()

    label1 = Label(root, text="Please enter the file path or choose a file:", fg="white", bg='black', font=20)
    label1.place(x=140, y=100)

    path_entry = Entry(root, bd=5, font=15, width=60)
    path_entry.bind(main)
    path_entry.place(x=140, y=140)

    # Button to browse through directories
    browse_btn = Button(root, text='Choose File', font=("Arial", 16), pady=6, width=10, bd=-2,
                        command=lambda: browse_pic(root))
    browse_btn.place(x=705, y=140)

    convrt_btn = Button(root, text="Convert", font=("Arial", 20), width=10, padx=5, pady=5, command=main)
    convrt_btn.place(x=340, y=180)

    success = Label(root, text='', bg='black')
    success.pack(pady=5)
    success.place(x=260, y=220)

    root.mainloop()
