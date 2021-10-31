# Animated ASCII Text: Bounce on edges
# Requires Pyfiglet Installation
# Press Ctrl + C to exit the animation
# Examples:
#   python animated.py
#   python animated.py -text ZTM

import pyfiglet, argparse, os, time

parser = argparse.ArgumentParser()
parser.add_argument('-text', required=False)
args = parser.parse_args()
text = getattr(args, 'text') or input("Text: ")
fig = pyfiglet.figlet_format(text)

fig = fig.split("\n")
fig.remove("")

cols, rows = os.get_terminal_size()
figcols, figrows = len(fig[0]), len(fig)


def draw(fig, cols, rows, figcols, figrows, left, top):
	hborder = "#" * cols
	bottom = rows - 2 - top - figrows
	right = cols - 4 - left - figcols
	empty_row = "##" + " " * (cols - 4) + "##\n"
	text_lines = ["##" + " " * left + line + " " * right + "##" for line in fig]
	text_lines = "\n".join(text_lines)
	fig = hborder + "\n" + empty_row * top + text_lines + "\n" + empty_row * bottom + hborder
	print(fig, end='')



left = 10
top = 10
deltaX = 1
deltaY = 1

while True:
	os.system("clear")
	draw(fig, cols, rows, figcols, figrows, left, top)
	
	left = left + deltaX
	top = top + deltaY
	
	bottom = rows - 2 - top - figrows
	right = cols - 4 - left - figcols
	
	if bottom == 0:
		deltaY = -1
	
	if top == 0:
		deltaY = 1
		
	if right == 0:
		deltaX = -1
		
	if left == 0:
		deltaX = 1
	
	
	
	
	time.sleep(0.07)