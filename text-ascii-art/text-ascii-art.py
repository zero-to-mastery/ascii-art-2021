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

args = parser.parse_args()

text = getattr(args, 'text') or input("Please enter the text you want to print: ")

print("Which font do you like?")
for i, _font in enumerate(fonts):
	# print 4 fonts in one line
	end = "\n" if (i + 1) % 4 == 0 else ""

	# pad the columns from their right 
	print(f"{(i+1)}.".ljust(4) +  f"{_font}".ljust(20, " "), end=end)

choice = int(input(f"\nYour choice between 1 and {len(fonts)}: "))

# Choose a font from the list of fonts
font = fonts[choice - 1]

print(f"Font: \t {choice} - {font}\n")

fig = pyfiglet.figlet_format(text, font=font)

print(fig)