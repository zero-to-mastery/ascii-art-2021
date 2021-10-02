"""
Dependencies: pyfiglet

Print the specified text as ASCII art using PyFiglet.

Command-line arguments:
	-text: text to be printed. Defaults to "ZTM" if not specified.
	-font: index of the font you want to use. Defaults to "standard" if not specified.

Examples:
python text-ascii-art.py
python text-ascii-art.py -text "Zero TM" -font 21
python text-ascii-art.py -text "Pakistan" -font 16

"""

import pyfiglet 
import argparse

fonts = ['standard', '3-d', '5lineoblique', '6x10', '6x9', 'acrobatic', 'arrows', 'ascii___',
'avatar', 'banner', 'banner3-D', 'banner3', 'banner4', 'big', 'block',
'broadway', 'bubble', 'caligraphy', 'doh', 'doom', 'isometric1', 'isometric3',
'nancyj-underlined', 'smkeyboard', 'univers'] 

# Create the parser
parser = argparse.ArgumentParser()

# Add the arguments
parser.add_argument('-text', required=False)
parser.add_argument('-font', required=False)

args = parser.parse_args()

text = getattr(args, 'text') or "ZTM"
font = getattr(args, 'font') or 0

font = int(font)

if font >= len(fonts):
	print(f"Invalid font. Please choose between 1 and {len(fonts) - 1}.")
	print("Defaulting to standard font.\n")
	font = 0

# Choose a font from the list of fonts
style = fonts[font]

print(f"Font: \t {font} - {style}\n")

fig = pyfiglet.figlet_format(text, font=style)

print(fig)


