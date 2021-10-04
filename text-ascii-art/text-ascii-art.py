# This project requires pyfiglet installation ://pypi.org/project/pyfiglet/
# Prints the specified text as ASCII art using PyFiglet.
# Command-line arguments:
#     -text: text to be printed. Defaults to "ZTM" if not specified.
#     -font: index of the font you want to use. Defaults to "standard" if not specified.
# Examples:
# python text-ascii-art.py
# python text-ascii-art.py -text "ZTM" -font 21
# python text-ascii-art.py -text "ASCII ART" -font 16
# python text-ascii-art.py -text "Python3" -font standard

import pyfiglet 
import argparse

fonts_list = ['standard', '3-d', '5lineoblique', '6x10', '6x9', 'acrobatic', 'arrows', 'ascii___',
'avatar', 'banner', 'banner3-D', 'banner3', 'banner4', 'big', 'block',
'broadway', 'bubble', 'caligraphy', 'doh', 'doom', 'isometric1', 'isometric3',
'nancyj-underlined', 'smkeyboard', 'univers'] 

def font_checker(fonts_list,fc=None):
    if isinstance(fc, int)==False:
                print("Which font do you like?")
                for i, _font in enumerate(fonts_list):
                    # print 4 fonts in one line
                    end = "\n" if (i + 1) % 4 == 0 else ""

                    # pad the columns from their right 
                    print(f"{(i+1)}.".ljust(4) +  f"{_font}".ljust(20, " "), end=end)

                choice = int(input(f"\nYour choice between 1 and {len(fonts_list)}: "))
    else:
                choice=fc

    # Choose a font from the list of fonts
    if 1<=choice and choice<=25:
        font = fonts_list[choice - 1]
    else:
        font=font_checker(fonts_list)

    print(f"Font: \t {choice} - {font}\n")
    return font

# Create the parser
parser = argparse.ArgumentParser()

# Add the arguments
parser.add_argument('-text', required=False)
parser.add_argument('-font', required=False)


args = parser.parse_args()

text = getattr(args, 'text') or input("Please enter the text you want to print: ")

font = getattr(args, 'font') or font_checker(fonts_list)

if font in fonts_list:
    print("Found your font!")
else:
    try:
        x=int(font)
        if 1<=x and x<=25:
            font = font_checker(fonts_list,x)
        else:
            font = font_checker(fonts_list)
    except ValueError:
        print("sorry,this font is not available")
        font = font_checker(fonts_list)

fig = pyfiglet.figlet_format(text, font=font)

print(fig)
