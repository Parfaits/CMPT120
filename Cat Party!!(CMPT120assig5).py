'''
Welcome to my cat party 2016
Made by none other than MEEEEEEEEEEow! (worked on my own) (^.w.^)
Johnny Doan
c = color
r = random
'''
import turtle as t
from random import randint, choice

turt = t.Turtle(shape='turtle')
cMode = t.colormode(255)
cPen = turt.pencolor('red')


def info():
	print('Made by none other than MEEEEEEEEEEow! \
		(worked on my own) (^.w.^) (Johnny Doan)')
	print('Sometimes I dream about cheese.')
	return


def rColors():
	red = randint(0, 255)
	green = randint(0, 255)
	blue = randint(0, 255)
	return red, green, blue


def canvasSize(x, y):
	turt.setposition(randint(x, y), randint(x, y))
	return


def square(l):
	# For the main loop. Called in rSquares()
	for i in range(4):
		turt.forward(l)
		turt.left(90)
	return


def rText(x, y):
	# For main loop. Called in rCirclePositions()
	for m in range(3):
		turt.penup()
		canvasSize(x, y)
		turt.setheading(0)
		turt.pendown()
		turt.color(rColors())
		turt.write('meow', font=("Arial", 16, "bold"))
	return


def rCirclePositions(x, y):
	# For main loop. Called in rSquares()
	for n in range(3):
		turt.fillcolor(rColors())
		turt.penup()
		canvasSize(x, y)
		turt.pendown()
		turt.begin_fill()
		turt.circle(20)
		turt.color(rColors())
		turt.end_fill()
	rText(x, y)
	return


def rSquares(l, x, y):
	# For main loop
	for s in range(3):
		turt.penup()
		canvasSize(x, y)
		turt.pendown()
		square(l)
		turt.color(rColors())
	rCirclePositions(x, y)
	return


def drawSquare(size):
	# For the freeDraw game
	for squr in range(4):
		turt.forward(size)
		turt.left(90)
	return


def freeDraw():
	x = 0
	y = 0
	print('Welcome to freeDraw Beta where you can move \
your turtle anywhere you like inside the boundary! :D Please stay in the boundary or turtle will die D:\n')
	while x < 10 or y < 10:
		try:
			skip = input('Skip setting up canvas size?(y/n)(default 360x360)_')
			if skip in ['n', 'no']:
				x = int(input('First enter canvas size length (actual divide by 2, \
must be greater than 10)_'))
				y = int(input('Second enter canvas size height (actual divide by 2, \
must be greater than 10)_'))
				if x < 10 or y < 10:
					print('Sorry, can\'t have negative numbers or less than 10.')
			elif skip in ['y', 'yes']:
				x = 180
				y = 180
			else:
				print('Huh?')
		except ValueError:
			print('Error, isNaN.')
	print('How to play:\nEnter these commands to move the turtle:\n\
\'w\' move forward\n\'d\' turn right\n\'s\' move backwards\n\
\'a\' turn left\n\'r\' to restart canvas\n\'q\' to exit freeDraw\n\
\'set\' to set the position of the turtle\n\'pu\' pick turtle up\n\
\'pd\' puts turtle back on canvas\n\'fill\' start point of filling with color\n\
\'endfill\' end point of fill\n\
Preset shapes:\n\'square\' draw a square\n\'circle\' draw a circle\n\
\'write\' write some text\n\
Too lazy to make more commands (^-.-^). Welp, have FUN!!!\n')
	print('Loading...\n')
	turt.clear()
	turt.penup()
	turt.setposition(-x, -y)
	turt.pendown()
	turt.forward(x*2)
	turt.left(90)
	turt.forward(y*2)
	turt.left(90)
	turt.forward(x*2)
	turt.left(90)
	turt.forward(y*2)
	turt.penup()
	turt.setposition(0, 0)
	turt.setheading(0)
	turt.pendown()
	while True:
		if -x <= int(turt.xcor()) <= x:
			if -y <= int(turt.ycor()) <= y:
				print('Your turtle is now at position: \
({:d},{:d})\n\n\n'.format(round(turt.xcor()), round(turt.ycor())))   # Trace where turtle is
				move = input('_').lower()
				if move == 'w':
					try:
						distance = int(input('Distance_'))
						turt.forward(distance)
						turt.color(rColors())
					except ValueError:
						print('Command cancelled. Not a number.')
					continue
				elif move == 'd':
					try:
						angle = int(input('Turn angle_'))
						turt.right(angle)
					except ValueError:
						print('Command cancelled. Not a number.')
					continue
				elif move == 's':
					try:
						distance = int(input('Distance_'))
						turt.backward(distance)
						turt.color(rColors())
					except ValueError:
						print('Command cancelled. Not a number.')
					continue
				elif move == 'a':
					try:
						angle = int(input('Turn angle_'))
						turt.left(angle)
					except ValueError:
						print('Command cancelled. Not a number.')
					continue
				elif move == 'q':
					print('Hope you had fun! Come again anytime! :D :3')
					break
				elif move == 'r':
					turt.clear()
					turt.penup()
					turt.setposition(-x, -y)
					turt.pendown()
					turt.forward(x*2)
					turt.left(90)
					turt.forward(y*2)
					turt.left(90)
					turt.forward(x*2)
					turt.left(90)
					turt.forward(y*2)
					turt.penup()
					turt.setposition(0, 0)
					turt.setheading(0)
					turt.pendown()
					continue
				elif move == 'set':
					try:
						posx = int(input('Turtle position (xcor)_'))
						posy = int(input('Turtle position (ycor)_'))
						turt.penup()
						turt.setposition(posx, posy)
						turt.pendown()
					except ValueError:
						print('Command cancelled. Not a number.')
					continue
				elif move in ['penup', 'pup', 'pu']:
					print('You pick up your turtle.')
					turt.penup()
					continue
				elif move in ['pendown', 'pdown', 'pd']:
					print('You place your turtle down.')
					turt.pendown()
					continue
				elif move in ['square', 'box']:
					try:
						size = int(input('Square size_'))
						fill = input('Fill with color?(y/n)_').lower()
						if fill in ['yes', 'y']:
							turt.fillcolor(rColors())
							turt.begin_fill()
							drawSquare(size)
							turt.end_fill()
						elif fill in ['no', 'n']:
							drawSquare(size)
						else:
							print('Command cancelled. Invalid command.')
					except ValueError:
						print('Command cancelled. Not a number.')
					continue
				elif move == 'circle':
					try:
						size = int(input('Circle radius_'))
						fill = input('Fill with color?(y/n)_').lower()
						if fill in ['yes', 'y']:
							turt.fillcolor(rColors())
							turt.begin_fill()
							turt.circle(size)
							turt.end_fill()
						elif fill in ['no', 'n']:
							turt.circle(size)
						else:
							print('Command cancelled. Invalid command.')
					except ValueError:
						print('Command cancelled. Not a number.')
					continue
				elif move in ['write', 'print', 'type']:
					word = input('What do you want turtle to print?_')
					cword = input('Want to add color?(y/n)(default is black)_')
					if cword in ['yes', 'y']:
						turt.setheading(0)
						turt.color(rColors())
						turt.write(word, move=True, font=('Arial', 16, 'bold'))
					elif cword in ['no', 'n']:
						turt.setheading(0)
						turt.color('black')
						turt.write(word, move=True, font=('Arial', 16, 'bold'))
					else:
						print('Command cancelled. Invalid command.')
					continue
				elif move in ['f', 'fill']:
					print('Turtle prepares itself...')
					turt.fillcolor(rColors())
					turt.begin_fill()
					continue
				elif move in ['ef', 'endfill']:
					print('Turtle uses \'COLORFUL BARF!!\'')
					turt.end_fill()
					continue
				else:
					print('Huh?')
					continue
				# OK no more commands i'm tired
		raise IndexError('Indexes out of bounds. YOU KILLED TURTLE!!! D\': *sobs in a corner*')
	return


def main(l=50, x=-180, y=180):
	# intializes the loading screen. Initializes first
	# rSquares() --> square() --> rCirclePositions() -->
	# rText()
	rSquares(l, x, y)
	return

# ========================= MAIN LOOP/LOADING SCREEN ==============
print('Hi There! And welcome to Cat Party 2016\nMake sure to play freeDraw!!!')
while True:
	print('Loading...')
	main()
	replay = input('Enter a command:\n\'c\' to reload \
:P\n\'m\' for more random fun :3 \n\'q\' to quit :(\n\
\'i\' for info :D\n\'fd\' to play freeDraw \(^.w.^)/\n_').lower()
	if replay == 'q':
		print('Aww you gotta go? 3: Well, see you soon! \(^.w.^)/meow.')
		break
	elif replay in ['fd', 'f', 'd', 'freedraw']:
		freeDraw()
		resume = input('\'r\' to go back to the party screen :D or just quit \'q\' >:(\n_')
		if resume == 'r':
			turt.clear()
			continue
		elif resume == 'q':
			print('Aww you gotta go? 3: Well, see you soon! \(^.w.^)/meow.')
			break
	elif replay == 'i':
		info()
		resume = input('\n\n\'r\' to resume or \'q\' to quit.\n_')
		if resume == 'r':
			continue
		elif resume == 'q':
			print('Aww you gotta go? 3: Well, see you soon! \(^.w.^)/meow.')
			break
	elif replay == 'c':
		turt.clear()
		continue
	elif replay == 'm':
		continue
	raise TypeError('YOU FOOL! THAT IS THE WRONG COMMAND! NOW \
YOU WILL PERISH BEFORE CODE KITTY!!! (**)(\',..,\')(**)HISSS')

turtPos = turt.pos()
print(turtPos)       # Just to trace where turt is.