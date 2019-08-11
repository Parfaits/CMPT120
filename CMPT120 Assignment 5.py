'''
Welcome to my cat party 2016
Made by none other than MEEEEEEEEEEow! (worked on my own) (^.w.^)
Johnny Doan
c = color
r = random
'''
import turtle as t
from random import randint, choice

random_int = randint(0, 255)
turt = t.Turtle(shape='turtle')
cMode = t.colormode(255)
cPen = turt.pencolor('red')


def rColors():
	red = randint(0, 255)
	green = randint(0, 255)
	blue = randint(0, 255)
	return red, green, blue


def canvasSize():
	turt.setposition(randint(-180, 180), randint(-180, 180))
	return


def square(l):
	for i in range(4):
		turt.forward(l)
		turt.left(90)
	return


def rText():
	for m in range(5):
		turt.penup()
		canvasSize()
		turt.setheading(0)
		turt.pendown()
		turt.color(rColors())
		turt.write('meow', font=("Arial", 16, "bold"))
	return


def rCirclePositions():
	for n in range(5):
		turt.fillcolor(rColors())
		turt.penup()
		canvasSize()
		turt.pendown()
		turt.begin_fill()
		turt.circle(20)
		turt.color(rColors())
		turt.end_fill()
	rText()
	return


def rSquares(l):
	# Gets drawn first then go up the functions in order :3
	for s in range(5):
		turt.penup()
		canvasSize()
		turt.pendown()
		square(l)
		turt.color(rColors())
	rCirclePositions()
	return

while True:
        rSquares(50)
        replay = input('Press \'c\' to clear and restart \
        :P\n\'m\' for more fun :3 \n\'q\' to quit :(\n\
           ').lower()
        if replay == 'q':
                break
        elif replay == 'c':
                turt.clear()
                continue
        elif replay == 'm':
                continue
        raise TypeError('YOU FOOL! THAT IS THE WRONG COMMAND! NOW TOU WILL PERISH BEFORE CODE CAT (**)(\',..,\')(**)')

print(rSquares(50))
turtPos = turt.pos()
print(turtPos)       # Just to trace where turt is.
