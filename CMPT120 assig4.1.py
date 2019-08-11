#1

def firstIsSmaller(meow, cat):
	if (type(meow) is int or type(meow) is str) and \
			(type(cat) is int or type(cat) is str):
		if meow < cat:
			return True
		else:
			return False
	else:
		return 'The cat fanatic was here! ;3'
print(firstIsSmaller(1, 10))

#2

def sum2(meow, cat):
	if type(meow) is int and type(cat) is int:
		return meow + cat
	else:
		return 'meow-your friendly cat fanatic! :3'

#3

def cookies(n):
	HugeBox = n // 48
	SmallBox = (n % 48) // 8
	unused = (n % 48) % 8
	profit = HugeBox*26 + SmallBox*4 - unused*2
	return '{0:d}..{1:d}..{2:d}..{3:d}'.format(HugeBox, SmallBox, unused, profit)

#4

def food(day, sweet):
	mourning = 'breakfast'
	noon = 'lunch'
	night = 'dinner'
	if type(day) is int and type(sweet) is bool:
		if 0 <= day <= 24:
			if day < 6:
				return 'no food'
			elif 6 <= day <= 10:
				if sweet is True:
					return '{:s},marmalade'.format(mourning)
				elif sweet is False:
					return '{:s},coffee'.format(mourning)
				else:
					return mourning
			elif 11 <= day <= 15:
				if sweet is True:
					return '{:s},dessert'.format(noon)
				else:
					return noon
			elif 15 < day < 22:
				if sweet is True:
					return '{:s},dessert'.format(night)
				else:
					return night
			else:
				return 'no food'
		else:
			return 'That\'s not within time.'
	else:
		return 'I only eat cat food :3\n     -From the person who is obsessed with cats or maybe is a cat o.o'

#5

def tooth(sweet, n):
	if type(sweet) is bool and type(n) is int: 
		if sweet is True:
			return 'You have a sweet tooth+{:d}!'.format(n)
		elif sweet is False:
			return 'You do not have a sweet tooth+{:d}!'.format(n)
	else:
		return 'Sometimes I dream about cats\n       -From the person who is obsessed with cats'
print(tooth(False, 0))

#6

def repeat_middle(meow):
	# made by the person who is obsessed with cats <(^._.^)>
	meow_str = str(meow)
	LenOfmeow = len(meow_str)
	if LenOfmeow >= 1:
		if LenOfmeow % 2 == 0:
			find_mid = (LenOfmeow-1) // 2
			doubles_repeat = meow_str[find_mid:find_mid+2]*LenOfmeow
			return doubles_repeat.center(len(doubles_repeat)+4, '!')
		else:
			find_mid = (LenOfmeow-1) // 2
			ones_repeat = meow_str[find_mid]*LenOfmeow
			return ones_repeat.center(len(ones_repeat)+2, '!')
	else:
		pass

#7

def first_last_repeated(orig, repet):
	repet_int = abs(int(repet))
	if len(orig) >= 1:
		return orig[0]*repet_int + ' ' + orig[-1]*repet_int
	else:
		pass

#8

def remainder_is_even(num, div):
	remainder = num % div
	if remainder % 2 == 0:
		return True
	else:
		return False

#9

def replaceCharAtPos(orig, pos):
    orig_str = str(orig)
    pos_int = int(pos)
    pos_str = str(pos_int)
    if len(orig_str) > pos_int:
        if pos_int >= 10:
            return orig_str[:pos_int] + pos_str[-1] + orig_str[pos_int+1:]
        else:
            return orig_str[:pos_int] + pos_str + orig_str[pos_int+1:]
    elif len(orig_str) <= pos_int:
        return orig_str
    else:
        return 'I did not understand you :P'
