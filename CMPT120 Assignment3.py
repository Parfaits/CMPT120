from math import sqrt
from time import sleep
import sys
'''
Password_Gen_3000

Made by: Johnny Doan (obsessed with cats)
I moved all my functions to the top so I could see it better
Had time to do a bit of decorating :P
Last revised: june 8 2016
Hours spent: 1hr
description: Interrogates the user for information then uses it to form a password :D
'''


def welcome_message(n):
	# A warm welcome message :P
	return 'Welcome! {:s}\n\nALRIGHT!! Now that you\'ve entered your information code kitty will now generate a password for you ;P.'.format(n)

def last_course_digit(last):
	# to see if the course after the "-" contains digits returns last digit or not
	if last[course_dash_find+1:].isdigit() is True:
		return last[-1]
	else:
		return ''


def pass_even(even):
	# to see if the password so far is even returns "E" or not
	if len(even) % 2 == 0:
		return 'E'
	else:
		return ''

# =========This block here is for interrogating the user ;3=====
print('This is the Password Gen 3000 machine!! :D.\nTo use please fill in the following questions.\n')
name = input('What is your name first and last name?: ')
age = input('What is your age?: ')
course = input('What course are you registered in?\nex: CMPT-120\n: ')
print(welcome_message(name))
try:
	input('Press \'Enter\' to continue...\n')
except SyntaxError:
	pass
# ============================================================

# =========This block is where code kitty makes the password
pass_a = name[1].upper()
name_space_find = name.find(' ')
pass_b = name[name_space_find+1:name_space_find+3]
pass_c = name[-1]
pass_d = '*'*int(age[0])
if int(age) >= 10:
        pass_d = '*'*int(age[0])
else:
        pass_d = ''
pass_e = '$'*int(sqrt(int(age)))
course_dash_find = course.find('-')
pass_f = course[course_dash_find-1:course_dash_find]
pass_g = last_course_digit(course)
pass_upto_g = pass_a+pass_b+pass_c+pass_d+pass_e+pass_f+pass_g
pass_h = pass_even(pass_upto_g)
# ========PASSWORD FORMATION FUSION HAAAAAAAAAAAAAA!!!! meow o.o

# fancy way of buffering '...' in one line
dot = '.'
sys.stdout.write('Code Kitty working')
for i in range(0, 3):
	sys.stdout.write(dot)
	sys.stdout.flush()   # forces each '.' to buffered
	sleep(1)
sys.stdout.write('<(^._.^)>')

# results to show user
print('\nTRACE - sqrt of age is: ', sqrt(float(age)))
print("\n\nMeow! (translate to \"Here is your password! :3\"): " + pass_a+pass_b+pass_c+pass_d+pass_e+pass_f+pass_g+pass_h)
print('\n\nCode kitty will go back to sleep now BYEE!!!!:D\nOnly regret...not enough time to add more cats :(')
