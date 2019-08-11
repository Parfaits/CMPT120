
def changeAchar(orig, ch1, ch2):
    # Meow :3
    list_orig = list(orig)
    if ch1 in list_orig:
        for n, i in enumerate(list_orig):
            if ch1 in i:
                # Should cover cases (lower and upper letters)
                list_orig[n] = ch2
        return ''.join(list_orig)
    else:
        return orig
print(changeAchar("1A---aa", "a", '2'))



def maxDigs(meow):
    meowList = list(meow)
    out = []
    try:
        for i in meow:
            if i.isdigit() is True:
                out.append(i)
                out = [int(n) for n in out]
        return max(out)
    except ValueError:
        # Takes care of empty list
        return -1
print(maxDigs("v"))



def giveMeUnitPos(st, ch):
	meow = ''
	for i in range(len(st)):
		str_i = str(i)
		if ch in st[i]:
			if i >= 10:
				meow += '..' + str_i[-1]
			else:
				meow += '..' + str(i)
		else:
			meow = meow
	return meow + '..'
print(giveMeUnitPos('abcdabcdabcdabcd', 'a'))



def addDigitsInString(meow):
	# MEOW :D
	meowEmpty = 0
	for i in meow:
		if i.isdigit() is True:
			meowEmpty += int(i)
	return meowEmpty
print(addDigitInString('.......'))



def digits_plus(meow):
	meowEmpty = ''
	if 0 <= meow <= 9:
		for i in range(meow+1):
			meowEmpty += str(i) + '+'
		return meowEmpty
	else:
		return 'MEOW :3'
print(digits_plus(4))


def count_digits(meow):
	catEmpty = ''
	for i in meow:
		if i.isdigit() is True:
			catEmpty += i
	return len(catEmpty)
print(count_digits('..1...1...1...1...'))



def inBetween(meow):
	catEmpty = ''
	for i in meow:
		catEmpty += i + '*'
	return catEmpty
print(inBetween(''))
