

def avgOdd(meow):
	zero = 0
	i = 0.0
	mepty = 0
	while zero < len(meow):
		if meow[zero].isdigit() and (not (int(meow[zero]) % 2 == 0)):
			i += int(meow[zero])
			mepty += 1
		zero += 1
	if mepty == 0:
		mepty = 1
	return i / mepty
print(avgOdd('1235'))


def countLowerFromUnil(st, start):
	mepty = 0
	while start < len(st):
		if st[start].isalpha() and st[start].islower():
			mepty += 1
		elif st[start].isdigit():
			break
		start += 1
	return mepty
print(countLowerFromUnit("ABCxAxx1aa",0))


def countLower(meow):
	zero = 0
	cat = 0
	while cat < len(meow):
		if meow[cat].isalpha() and meow[cat].islower():
			zero += 1
		cat += 1
	return zero
print(countLower('123AA'))


def immPairsBool(meow):
	cat = False
	zero = 1
	while zero < len(meow):
		if meow[zero] == meow[zero-1]:
			cat = True
		zero += 1
	return cat
print(immPairsBool('123xx321'))


def immPairs(meow):
	cat = 1
	zero = 0
	while cat < len(meow):
		if meow[cat] == meow[cat-1]:
			zero += 1
		cat += 1
	return zero
print(immPairs('abxxxab88ef'))


def searchVowel(meow):
	cat = 0
	catnip = False
	while cat < len(meow):
		if meow[cat].lower() in ['a', 'e', 'i', 'u', 'o']:
			catnip = True
		cat += 1
	return catnip
print(searchVowel('A'))


def avgBackw(meow):
	zero = 0
	i = 0.0
	cat = len(meow) - 1
	while cat >= 0:
		if meow[cat].isdigit():
			i += int(meow[cat])
			zero += 1
		elif meow[cat].isalpha():
			break
		cat -= 1
	if zero == 0:
		zero = 1
	return i / zero
print(avgBackw('as40'))


def triple(meow):
	zero = 0
	mepty = ''
	while zero < len(meow):
		if meow[zero].isdigit() and int(meow[zero]) % 3 == 0:
			mepty += meow[zero] * 3
		else:
			mepty += meow[zero]
		zero += 1
	return mepty
print(triple(' '))


def same_substring(a, b):
	cat = 0
	meow = 0
	while cat < len(a) - 1:
		if a[cat:cat+2] in b:
			meow += 1
		cat += 1
	return meow
print(same_substring('zyxxyz', 'yyxxyyxx'))


def counteven(meow):
	cat = 0
	Teo = 0
	while cat < len(meow):
		if meow[cat].isdigit() and int(meow[cat]) % 2 == 0:
			Teo += 1
		cat += 1
	if Teo == 0:
		Teo = 'No Evens!'
	return Teo
print(counteven('meow1'))


def bear(meow):
	cat = 0
	Teo = 0
	Lich = 0
	Iranoutofcatnames = False
	while cat < len(meow):
		if 'bear' in meow[cat:cat+4].lower():
			Teo += 1
		elif 'lion' in meow[cat:cat+4].lower():
			Lich += 1
		cat += 1
	if Teo == Lich:
		Iranoutofcatnames = True
	return Iranoutofcatnames
print(bear('123abear213alionlion'))


def mini(me, o, w):
	cat = 0
	Lich = 9
	Teo = ''
	while cat < len(me):
		if me[cat].isdigit():
			Teo += me[cat]
		if me[cat].isdigit() and int(me[cat]) <= Lich:
			Lich = int(me[cat])
		cat += 1
	if o <= Lich and o <= w:
		Lich = o
	elif w <= Lich and w <= o:
		Lich = w
	if Teo == '':
		Lich = -1
	return Lich
print(mini('2', 1, 2))

================STAR=================
def sumOfPos(st, ch):
	meow = 0
	cat = 0
	Teo = ''
	while cat < len(st):
		if st[cat].isalpha() and ch not in st[cat]:
			meow += cat
			Teo += st[cat]
		cat += 1
	if len(Teo) == 0:
		meow = -1
	return meow
print(sumOfPos('123w', 'w'))


def easyLOL101(st, intt):
	meow = ''
	cat = 0
	Teo = intt
	while Teo < len(st) and len(meow) < 1:
		if st[Teo].isdigit() and int(st[Teo]) % 2 == 0:
			meow += st[Teo]
			cat += Teo
		Teo += 1
	if intt >= len(st) or meow == '':
		meow = 'no even number'
	else:
		meow += ',' + str(cat)
	return meow
print(easyLOL101('2meow132', 0))


def frown(meow):
	cat = 0
	Teo = ''
	while cat < len(meow):
		if ':(' in meow[cat:cat+2]:
			Teo += ':)'
		else:
			Teo += meow[cat]
		cat += 1
	return Teo
print(frown('m:(:('))
