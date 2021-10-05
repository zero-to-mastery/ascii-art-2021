"""
This module uses tkinter.
For installation instructions, see https://tkdocs.com/tutorial/install.html
"""
import tkinter as tk
from tkinter import *
from tkinter import filedialog
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
    success.config(
        text='Image converted successfully! File saved as \'output.txt\'', fg='white')  # Success message displays upon conversion


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("900x500")
    root.title("Image to ASCII converter")
    root.configure(background="black")
    root.resizable(0, 0)

    def browsePic():  # Allows user to browse directories for file and provides path to entry1
        global entry1
        tempdir = filedialog.askopenfilename(parent=root, filetypes=(
            ('png files', '*.png'), ('jpeg files', '*.jpg'), ('all files', '*.*')), title='Please select a file')
        entry1.insert(tk.END, tempdir)

    Label(root, text="Image to ASCII Converter", fg="black",
          font=("Times", 25, "bold"), width=25, pady=5, padx=25).pack()

    label1 = Label(root, text="Please enter the file path or choose a file:",
                   fg="white", bg='black', font=(20))
    label1.place(x=140, y=100)

    entry1 = Entry(root, bd=5, font=(15), width=60)
    entry1.bind(main)
    entry1.place(x=140, y=140)

    browse_btn = tk.Button(root, text='Choose File', font=("Arial", 16), pady=6,
                           width=10, bd=-2, command=browsePic)  # Button to browse through directories
    browse_btn.place(x=705, y=140)

    convrt_btn = Button(root, text="Convert", font=("Arial", 20),
                        width=10, padx=5, pady=5, command=main)
    convrt_btn.place(x=340, y=180)

    success = Label(root, text='', bg='black')
    success.pack(pady=5)
    success.place(x=260, y=220)

    root.mainloop()
