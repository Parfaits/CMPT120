'''
Made by MEEEEEEEEEEEEOW
 Johnny Doan 301289781
 finished Jul 30 2016
 Last Modified Aug 7 2016'''
from random import randint
import sys
from time import sleep

board = []  # Main board where all the modification
titled_board = [['\t']]  # printed board
colors = {
			# Made a dictionary just so I can switch
			# Back and forth between easily
			'black': '1',
			'white': '0',
			'1': 'black',
			'0': 'white'
}


def askBoardSize():
	'''
	^does what the title says
	try catch to ensure our user enter correctly
	(another way of validating) also diana said it ok :)
	'''
	ask_dim = 0
	while not(3 <= ask_dim <= 6):
		try:
			ask_dim = int(input('Size of board? (between 3 and 6 inclusive)_'))
		except ValueError:
			print('Error! IsNaN. Try again.')
		else:
			if not(3 <= ask_dim <= 6):
				print('That is not the appropriate size, try again :P')
	return ask_dim


def createTitledBoard():
	'''
	As the function name says
	will append the contents of board
	to titled_board and print it then erase
	so that it would prepare for the new modified board
	'''
	for n in range(len(board)):
		titled_board.append(['row{:d}\t'.format(n)])
		titled_board[0].append('column{:d}\t\t'.format(n))
	for row in range(len(board)):
		for column in range(len(board[row])):
			titled_board[row+1].append(board[row][column]+'\t\t')
	for mat in titled_board:
		print(''.join(mat))
	del titled_board[:]
	titled_board.append(['\t'])
	return


def createBoard(size):
	'''
	^Says it all uses size to make random 0 1 matrix skeleton to board
	'''
	for rows in range(size):
		board.append([])
		for column in range(size):
			board[rows].append(str(randint(0, 1)))
	return


def color():
	'''
	ask user to pick 1 of the options black or white
	'''
	blackwhite = ''
	while blackwhite not in ['1', '0', 'black', 'white']:
		blackwhite = input('What color do you want to play as?\n\n1 - black\n0 - white\n\n_').lower()
		if blackwhite not in ['1', '0', 'black', 'white']:
			print('Sorry, that\'s not an option. :P\n')
	if blackwhite == 'black':
		blackwhite = '1'
	elif blackwhite == 'white':
		blackwhite = '0'
	print('''You are playing as {:s} which is the \
{:s}\'s digits\nGOODLUCK HAVE FUN MEOW! :3\n'''.format(colors[blackwhite], blackwhite))
	return blackwhite


def chooseRow(size):
	'''
	title^ says it all user choose row
	try catch to guarantee user types correctly
	'''
	row = -1
	while not(row == 99) and not(0 <= row < size):
		try:
			row = int(input('row_'))
		except ValueError:
			print('Error! IsNaN. Try again')
		else:
			if not(row == 99) and not(0 <= row < size):
				print('Out of bounds. Please try again. :3')
	return row


def chooseColumn(size):
	'''
	same thing as chooseRow() but with columns
	'''
	column = -1
	while not(column == 99) and not(0 <= column < size):
		try:
			column = int(input('column_'))
		except ValueError:
			print('Error! IsNaN. Try again.')
		else:
			if not(column == 99) and not(0 <= column < size):
				print('Out of bounds. Please try again. :3')
	return column


def countRowCol(c, row, col):
	'''
	print ze row/col that have as many even of users color
	takes color (str), row (list), and column (list) arguments
	'''
	print('\nRows that have an even number of user digit\'s for player ({:s})\n'.format(colors[c]))
	if len(row) == 0:
		print('- None of the rows')
	else:
		for rid in range(len(row)):
			print('- row number ({:d})'.format(row[rid]))
	print('\nCols that have an even number of user digit\'s for player ({:s})\n'.format(colors[c]))
	if len(col) == 0:
		print('- None of the columns')
	else:
		for cid in range(len(col)):
			print('- column number ({:d})'.format(col[cid]))
	return


def score(color):
	'''
	Zeee score board :D meow
	where the score is calculated with the final board in a level and shown
	uses countRowCol() also tells user if they win/lose and how many points
	'''
	count_row = 0
	count_column = 0
	point_row = 0
	point_column = 0
	row_id = []
	column_id = []
	for row in range(len(board)):
		for column in range(len(board[row])):
			if board[row][column] == color:
				count_row += 1
			if board[column][row] == color:
				count_column += 1
		if count_row != 0 and count_row % 2 == 0:
			point_row += 1
			row_id.append(row)
		count_row = 0
		if count_column != 0 and count_column % 2 == 0:
			point_column += 1
			column_id.append(row)
		count_column = 0
	if point_row == 0 or point_column == 0:
		countRowCol(color, row_id, column_id)
		print('''\nSorry!  For you to win, the board had to have at least\n\
			one row and one col with an even number of your color,\n\
			your color was {:s} (digit {:s}).You are not awarded any points :P\n\
			CODE KITTY WINS!! ALL HAIL CODE KITTY \(^\'w\'^)/'''.format(colors[color], color))
		count_compwins.append(1)
	else:
		countRowCol(color, row_id, column_id)
		print('''\nCONGRATZ!! YOU WIN! Code Kitty loses 3:\
			\nYour color was {:s} (digit {:s})\n\nYou got {:d} row with an even number of {:s}\'s\n\
			and {:d} col with an even number of {:s}\'s\n\
			!!! Therefore, for this game you\'ve earned: {:d} points \
			!!!'''.format(colors[color], color, point_row, color, point_column, color, point_row+point_column))
		count_points[0] += point_row+point_column
		count_wins.append(1)
	return


def intermediateMove(r, c):
	'''
	Move changes for pvcIntermediate() game r = row c = column
	First for nest changes element starting from (r, c) to end of the column
	Second for nest changes element starting from (r, c) to end of the row
	'''
	for rows in range(r, r+1):
		for columns in range(c, len(board[rows])):
			if board[rows][columns] == '1':
				board[rows][columns] = '0'
			else:
				board[rows][columns] = '1'
	for ro in range(r+1, len(board)):
		for co in range(c, c+1):
			if board[ro][co] == '1':
				board[ro][co] = '0'
			else:
				board[ro][co] = '1'
	return


def advancedMove(r, c):
	'''
	Cross flip moves r = row c = column
	for pvcAdvanced()
	'''
	if r+1 < len(board):
		if board[r+1][c] == '1':
			board[r+1][c] = '0'
		else:
			board[r+1][c] = '1'
	if c+1 < len(board[r]):
		if board[r][c+1] == '1':
			board[r][c+1] = '0'
		else:
			board[r][c+1] = '1'
	if r-1 != -1:
		if board[r-1][c] == '1':
			board[r-1][c] = '0'
		else:
			board[r-1][c] = '1'
	if c-1 != -1:
		if board[r][c-1] == '1':
			board[r][c-1] = '0'
		else:
			board[r][c-1] = '1'
	if board[r][c] == '1':
		board[r][c] = '0'
	else:
		board[r][c] = '1'
	return


def singlePlayer(size):
	'''
	Otherwise known as level 1 (run by this main function)
	uses createBoard(), color(), createTitledBoard(),
	chooseColumn(), chooseRow(), score()
	funtions
	one main while loop for each level (each level have very similar skeleton)
	'''
	createBoard(size)
	move = 0
	colo = color()
	row = 0
	column = 0
	print('\t', '-'*17, '\n\t | Initial Board |\n', '\t', '-'*17)
	while move < size and not(row == 99 and column == 99):
		createTitledBoard()
		print('''\n\nYou have {:d} moves left.\n\
Enter in 99 for both row and column to forcefully end the game.'''.format(size-move))
		row = chooseRow(size)
		column = chooseColumn(size)
		while (row == 99 and column != 99) or (column == 99 and row != 99):  # The case where user may accidentally type a valid int
			print('I see you are trying to end game. But you have to put both row and column as 99. Try again!')
			row = chooseRow(size)
			column = chooseColumn(size)
		if row == 99 and column == 99:
			continue  # The rest will not be executed at this point and will exit loop do not confuse with break diana said it ok
		print('\nYou played ({:d}, {:d})\n'.format(row, column))
		if board[row][column] == '1':
			board[row][column] = '0'
		else:
			board[row][column] = '1'
		move += 1
	if row == 99:  # Since both row/col gonna be 99 anyways chose row
		print('\nThe game has been forcefully ended. The final board is shown!\n')
		createTitledBoard()
	else:
		print('\nThe game has ended! Here is your final board. :DANCE (｢`･ω･)｢ 乁( ˙ ω˙乁)\n')
		createTitledBoard()
	score(colo)
	return


def pvcIntermediate(size):
	'''
	Or known as level 2 pvc = player vs computer
	add on to functions in singlePlayer()
	we got randint() for computer moves, intermediateMove()
	'''
	createBoard(size)
	move = 0
	colo = color()
	row = 0
	column = 0
	print('\t', '-'*17, '\n\t | Initial Board |\n', '\t', '-'*17)
	while move < size and not(row == 99 and column == 99):
		comp_row = randint(0, size-1)
		comp_column = randint(0, size-1)
		createTitledBoard()
		print('''\n\nYou have {:d} moves left.\n\
Enter in 99 for both row and column to forcefully end the game.'''.format(size-move))
		row = chooseRow(size)
		column = chooseColumn(size)
		while (row == 99 and column != 99) or (column == 99 and row != 99):
			print('I see you are trying to end game. But you have to put both row and column as 99. Try again!')
			row = chooseRow(size)
			column = chooseColumn(size)
		if row == 99 and column == 99:
			continue
		print('\nYou played ({:d}, {:d})\n'.format(row, column))
		print('-'*25)
		intermediateMove(row, column)  # Player move
		createTitledBoard()
		print('\nComputer played ({:d}, {:d})\n'.format(comp_row, comp_column))
		print('-'*25)
		intermediateMove(comp_row, comp_column)  # Comp move
		move += 1
	if row == 99:
		print('\nThe game has been forcefully ended. The final board is shown!\n')
		createTitledBoard()
	else:
		print('\nThe game has ended! Here is your final board. :DANCE (｢`･ω･)｢ 乁( ˙ ω˙乁)\n')
		createTitledBoard()
	score(colo)
	return


def pvcAdvanced(size):
	'''
	Or level 3
	we got even mooore while loops this time HAHHA check out my sick whiles
	I know it is the most disgusting thing ever BUT it works :D
	just to verify player choose own color and that 99 exit xD
	and COMP choose own color too
	added a buffer so I don't overwhelm myself with
	alot of text at the start
	'''
	createBoard(size)
	move = 0
	colo = color()
	row = 0
	column = 0
	print('\t', '-'*17, '\n\t | Initial Board |\n', '\t', '-'*17)
	while move < size and not(row == 99 and column == 99):
		createTitledBoard()
		print('''\n\nYou have {:d} moves left.\n\
Enter in 99 for both row and column to forcefully end the game.'''.format(size-move))
		row = chooseRow(size)
		column = chooseColumn(size)
		while (row != 99 and column != 99) and board[row][column] != colo:  # Enforce user chooose own color or quit
			print('Sorry that is not your color. Choose another position. Your moves were not affected.')
			row = chooseRow(size)
			column = chooseColumn(size)
		while (row == 99 and column != 99) or (column == 99 and row != 99):  # Case: (99, 1)
			print('I see you are trying to end game. But you have to put both row and column as 99. Try again!')
			row = chooseRow(size)
			column = chooseColumn(size)
			while (row != 99 and column != 99) and board[row][column] != colo:
				# Case1: your colo = 1, (choose 1, 2), (1, 2) = 0. Enter this loop  < very useful comments I must say :3
				# Case2: (99, 1). Exit this and re-enter parent loop
				# Case3: (99, 99). Exit Both
				print('Sorry that is not your color. Choose another position. Your moves were not affected.')
				row = chooseRow(size)
				column = chooseColumn(size)
		if row == 99 and column == 99:
			continue
		advancedMove(row, column)  # Player move
		comp_row = randint(0, size-1)
		comp_column = randint(0, size-1)
		while board[comp_row][comp_column] == colo:  # Enforce comp choose own color
			comp_row = randint(0, size-1)
			comp_column = randint(0, size-1)
		print('\nYou played ({:d}, {:d})\n'.format(row, column))
		print('-'*25)
		createTitledBoard() 
		sys.stdout.write('\nComputer thinking')
		for i in range(3):
			sys.stdout.write('.')
			sys.stdout.flush()
			sleep(1)
		sys.stdout.write('\nComputer played ({:d}, {:d})\n\n'.format(comp_row, comp_column))
		print('-'*25)
		advancedMove(comp_row, comp_column)  # Comp move
		move += 1
	if row == 99:
		print('\nThe game has been forcefully ended. The final board is shown!\n')
		createTitledBoard()
	else:
		print('\nThe game has ended! Here is your final board. :DANCE (｢`･ω･)｢ 乁( ˙ ω˙乁)\n')
		createTitledBoard()
	score(colo)
	return 


def askToPlay():  # Title explains it all count_plays determines the question
	play = ''
	words = ['yes', 'no', 'n', 'y', 'meow', 'nya', 'nah', 'ok', 'ya', 'q', 'sure', 'quit']
	quit = ['n', 'no', 'nah', 'q', 'quit']
	while play not in words:
		if count_plays == 0:
			play = input('Want to play a game? Meow ฅ ̳͒•ˑ̫• ̳͒ฅ♡\nYes or no?\n_').lower()
		else:
			play = input('\nWant to play again?? Pretty pwease? ฅ(⌯͒• ɪ •⌯͒)ฅnya～ﾝ❣?\n_').lower()
		if play not in words:
			print('Huh?')
		elif count_plays == 0 and play in words and play not in quit:
			print('''WELCOME!!! TO FLIPPING DANCE GAME \n\
(I don\'t know why the prof named it this LOL)''')
			print('-'*50)
	if count_plays == 0 and play in quit:  # I got bored here and learned I could print kaomoji's HAHAHAHAHAHAHAHAHAHAHAHAHAHA
		'''
			You can choose to ignore this section haha
			This is just so if the user declines the initial ask to play (count_plays == 0)
			This will confirm one last time if they want to play (my own way of what diana did in sampleRun_no_play_at_all.txt)
		'''
		print('Wait w-w-wwhat do u mean you do not want to play? (ʘ言ʘ╬)')
		print('''PLEASE PLAY I WORKED SO HARD ON THISSS!!!! :\'(\n\
ヾ(｀ε´)ﾉ\nWAAAAAAAAAAA(ﾉꐦ ⊙曲ఠ)ﾉ彡┻━┻''')
		del play
		play = ''
		while play not in words:
			play = input('Please play? (ฅ•.•ฅ)\n_')
			if play in quit:
				print('*Cries in a corner*\n˚‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·˚')  # You meanie!!
			else:
				print('HOOOORAY!!!! ٩(˃̶͈̀௰˂̶͈́)و (و ˃̵ᴗ˂̵)و ✧*｡٩(ˊᗜˋ*)و✧*｡')
			if play not in words:
				print('Wait huh?')  
	return play


def chooseOptions():  # ask user to choose an option (Main menu)
	ask_option = ''
	while ask_option not in ['1', '2', '3']:
		print('\t\tFLIPPING DANCE ALPHA')
		print('\t\t'+'-'*20)
		ask_option = input('''\n\t\t\t1 - Single Player (level1)\n\
\t\t\t2 - Player vs Computer (Intermediate Level2)\n\
\t\t\t3 - Player vs Computer (Advanced Level3)\n\nOption_''')
		if ask_option not in ['1', '2', '3']:
			print('Umm, that is not an option.')
	return ask_option

# =========================TOP MEEEEEEEEEEEEOW!!!!!===============
count_plays = 0       # }
count_wins = []       #
count_compwins = []   # Ze score board :3
count_points = [0]    #
board_value = 0       # }

playing = askToPlay()
quit = ['n', 'no', 'nah', 'q', 'quit']
'''
^I put all these global vars here so it's easier to see and work with.
Please understand that it makes it easier for me to have these variables here
just to debug so I don't have to scroll all the way up
'''
while playing not in quit:  # Main loop
	options = chooseOptions()
	board_size = askBoardSize()
	if options == '1':
		singlePlayer(board_size)
	elif options == '2':
		pvcIntermediate(board_size)
	elif options == '3':
		pvcAdvanced(board_size)
	count_plays += 1
	playing = askToPlay()
	
	if playing not in quit:   # refresh board after eachgame keeps final board
		del board[:]
		print('You\'ve completed {:d} games so far. Keep going! ฅ(*°ω°*)ฅ '.format(count_plays))
		#  ^Trace how many games played so far
	if playing in quit:  # The final act before loop finishes
		for dec in range(len(board[0])):  # calculate 'Board value'
			board_value += (2**(len(board[0])-dec-1)) * int(board[0][dec])
		print('THE END GAME SCORE BOARD IS HERE! MUAHAAHAH ฅ(*°ω°*)ฅ')
		print('-'*80)
		print('Here is your final board you\'ve  played last :\n')
		createTitledBoard()  # Trace if I actually have the final board
		print('\nTotal points user in all games:  {:d}'.format(count_points[0]))
		print('Total games user played:  {:d}'.format(count_plays))  # Trace games played
		print('Total games the user won:  {:d}'.format(len(count_wins)))
		print('Total games the computer won:  {:d}'.format(len(count_compwins)))
		print('Board value of last board\'s first row in decimal:  {:d}'.format(board_value))
		input('This is the end of the game! Hope you like ฅ ̳͒•ˑ̫• ̳͒ฅ♡\npress \'Enter\' to finish.\n_')
# just a little extra at the end of my insanity HAHAHAHAHAHAHAH jk plz don't hurt me
print('FINE! You won\'t play ฅ⁽͑ ˚̀ ˙̭ ˚́ ⁾̉ฅ\nThat\'s it!')
print('''──────▄▀▀▄────────────────▄▀▀▄────
─────▐▒▒▒▒▌──────────────▌▒▒▒▒▌───
─────▌▒▒▒▒▐─────────────▐▒▒▒▒▒▐───
────▐▒▒▒▒▒▒▌─▄▄▄▀▀▀▀▄▄▄─▌▒▒▒▒▒▒▌──
───▄▌▒▒▒▒▒▒▒▀▒▒▒▒▒▒▒▒▒▒▀▒▒▒▒▒▒▐───
─▄▀▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌───
▐▒▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───
▌▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌──
▒▒▐▒▒▒▒▒▒▒▒▒▄▀▀▀▀▄▒▒▒▒▒▄▀▀▀▀▄▒▒▐──
▒▒▌▒▒▒▒▒▒▒▒▐▌─▄▄─▐▌▒▒▒▐▌─▄▄─▐▌▒▒▌─
▒▐▒▒▒▒▒▒▒▒▒▐▌▐█▄▌▐▌▒▒▒▐▌▐█▄▌▐▌▒▒▐─
▒▌▒▒▒▒▒▒▒▒▒▐▌─▀▀─▐▌▒▒▒▐▌─▀▀─▐▌▒▒▒▌
▒▌▒▒▒▒▒▒▒▒▒▒▀▄▄▄▄▀▒▒▒▒▒▀▄▄▄▄▀▒▒▒▒▐
▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄▄▒▒▒▒▒▒▒▒▒▒▒▐
▒▌▒▒▒▒▒▒▒▒▒▒▒▒▀▒▀▒▒▒▀▒▒▒▀▒▀▒▒▒▒▒▒▐
▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▀▒▒▒▄▀▄▒▒▒▀▒▒▒▒▒▒▒▐
▒▐▒▒▒▒▒▒▒▒▒▒▀▄▒▒▒▄▀▒▒▒▀▄▒▒▒▄▀▒▒▒▒▐
▒▓▌▒▒▒▒▒▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▐
▒▓▓▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌
▒▒▓▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─
▒▒▓▓▀▀▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──
▒▒▒▓▓▓▓▓▀▀▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄▀▀▒▌─
▒▒▒▒▒▓▓▓▓▓▓▓▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▒▒▒▒▒▐─
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌
▒▒▒▒▒▒▒█▒█▒█▀▒█▀█▒█▒▒▒█▒█▒█▒▒▒▒▒▒▐
▒▒▒▒▒▒▒█▀█▒█▀▒█▄█▒▀█▒█▀▒▀▀█▒▒▒▒▒▒▐
▒▒▒▒▒▒▒▀▒▀▒▀▀▒▀▒▀▒▒▒▀▒▒▒▀▀▀▒▒▒▒▒▒▐
▒█▀▄▒█▀▄▒█▀▒█▀█▒▀█▀▒█▒█▒█▒█▄▒█▒▄▀▀▐
▒█▀▄▒█▀▄▒█▀▒█▄█▒▒█▒▒█▀█▒█▒█▀██▒█▒█▐ 
▒▀▀▒▒▀▒▀▒▀▀▒▀▒▀▒▒▀▒▒▀▒▀▒▀▒▀▒▒▀▒▒▀▀▐
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒﻿''')
print('CODE KITTY USES OVERFLOW ERROR!!!!\n\n')  # I'm scared to actually raise an error might get marked wrong LOL
print('raise OverflowError(\'SUPER EFFECTIVE!ERROR! ERROR! TOO MUCH CATS!!!\')')
# This marks the end of the program :3
