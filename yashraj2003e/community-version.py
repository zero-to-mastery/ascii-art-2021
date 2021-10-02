import tkinter.messagebox as ms
import PIL.Image
from tkinter import *
from tkinter import font
import sys

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
    try:
        with open("output.txt", "w") as text_file:
            text_file.write(txt)
    except:
        return

def handle_image_conversion(image_filepath):
    image = None
    try:
        image = PIL.Image.open(image_filepath)
    except Exception as err:
        ms.showerror("Oops !","Unable to open image file !")
        root.destroy()
        return

    ascii_img = convert_image_to_ascii(image)
    return ascii_img

def main():
    global entry1
    try:
        image_file_path = sys.argv[1]
    except IndexError:
        image_file_path = entry1.get()
    ascii_img = handle_image_conversion(image_file_path)
    print(ascii_img)
    write_to_txtfile(ascii_img)

root=Tk()
root.geometry("800x220")
root.title("Image to ASCII converter")
root.configure(background="black")
root.resizable(0,0)

Label(root, text = "Image to ASCII Convertor",fg="black",font=("Times",25,"bold"),width=25).pack()

label1 = Label(root, text = "Please enter file path - ",fg="black",font=(15))
label1.place(x=80,y=60)

entry1=Entry(root,bd = 5,font = (15),width=70)
entry1.bind(main)
entry1.place(x=80,y=100)

button1= Button(root,text= "Convert",font=("Times",20),width=10,padx=5,pady=5,command=main)
button1.place(x=310,y=150)

root.mainloop()
