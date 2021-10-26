# This project requires pyfiglet installation ://pypi.org/project/pyfiglet/
# This project also requires termcolor and colorama. Install them by running pip install termcolor, colorama
# Prints the specified text as ASCII art using PyFiglet.
# Command-line arguments:
#     -text: text to be printed. Defaults to "ZTM" if not specified.
#     -font: index of the font you want to use. Defaults to "standard" if not specified.
#     -color: text color. Defaults to "None" if not specified.
#     -attrs: attributes (comma-separated) used for the style. Defaults to "None" if not specified.
# Examples:
# python text-ascii-art.py
# python text-ascii-art.py -text "ZTM" -font 21
# python text-ascii-art.py -text "ASCII ART" -font 16
# python text-ascii-art.py -text "Python3" -font standard
# python text-ascii-art.py -text "Bold" -font standard -attrs bold,underline
# python text-ascii-art.py -text "ZTM" -font isometric3 -color green
# python text-ascii-art.py -text "Colorama" -font isometric3 -color red -attrs bold

import pyfiglet
import argparse
import termcolor, colorama

colorama.init()

fonts_list = ['standard', '3-d', '5lineoblique', '6x10', '6x9', 'acrobatic', 'arrows', 'ascii___',
'avatar', 'banner', 'banner3-D', 'banner3', 'banner4', 'big', 'block',
'broadway', 'bubble', 'caligraphy', 'doh', 'doom', 'isometric1', 'isometric3',
'nancyj-underlined', 'smkeyboard', 'univers']

colors_list = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
attrs_list = ['bold', 'dark', 'underline', 'blink', 'reverse', 'concealed']
attrs_valid = []

def font_checker(fonts_list, fc=None):
    if not isinstance(fc, int):
        print("Which font do you like?")
        for i, _font in enumerate(fonts_list):
            # print 4 fonts in one line
            end = "\n" if (i + 1) % 4 == 0 else ""

            # pad the columns from their right 
            print(f"{(i+1)}.".ljust(4) +  f"{_font}".ljust(20, " "), end=end)

        choice = int(input(f"\nYour choice between 1 and {len(fonts_list)}: "))
    else:
        choice = fc

    # Choose a font from the list of fonts
    if 1 <= choice and choice <= 25:
        font = fonts_list[choice - 1]
    else:
        font = font_checker(fonts_list)

    print(f"Font: \t {choice} - {font}\n")
    return font

def validate_color(color):
    global colors_list
    if color not in colors_list:
        print(f"Invalid color: {color}.")
        print(f"Choose one of {', '.join(colors_list)}.")
        color = input("Please enter a color: ")
        validate_color(color)

    return color

def validate_attrs(attrs):
    global attrs_list
    global attrs_valid
    
    if attrs is not None:
      for attr in attrs:
        if attr not in attrs_list:
            print(f"Invalid attribute: {attr}.")
            print(f"Choose one of {', '.join(attrs_list)}.")
            attr = input("Please enter an attribute: ")
            attr = validate_attrs(attr.split(","))
        else:
          attrs_valid.append(attr)
    
    return attrs_valid    

# Create the parser
parser = argparse.ArgumentParser()

# Add the arguments
parser.add_argument('-text', required=False)
parser.add_argument('-font', required=False)
parser.add_argument('-color', required=False)
parser.add_argument('-attrs', required=False)

args = parser.parse_args()

text = getattr(args, 'text') or input("Please enter the text you want to print: ")

font = getattr(args, 'font') or font_checker(fonts_list)

color = getattr(args, 'color')
attrs = (getattr(args, 'attrs'))
if attrs is not None:
  attrs = attrs.split(',')

if font not in fonts_list:
    try:
        x = int(font)
        if x >= 1 and x <= 25:
            font = font_checker(fonts_list, x)
        else:
            font = font_checker(fonts_list)
    except ValueError:
        print("Sorry, this font is not available")
        font = font_checker(fonts_list)

fig = pyfiglet.figlet_format(text, font=font)

if color is not None:
    color = validate_color(color)
if attrs is not None:
    attrs = validate_attrs(attrs)

print(termcolor.colored(fig, color, attrs=attrs))