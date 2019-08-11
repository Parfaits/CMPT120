

def createListDim(dim):
	meow = []
	for i in range(dim):
		meow.append(i*10)
	return meow
print(createListDim(4))


def createMatDimXDim(dim):
	meow = []
	for row in range(dim):
		meow.append([])
		for column in range(dim):
			meow[row].append(row*10+column)
	return meow
print(createMatDimXDim(4))


def addValuesInAllRows(meow):
	cat = []
	Teo = 0
	for row in range(len(meow)):
		for column in range(len(meow[row])):
			Teo += meow[row][column]
		cat.append(Teo)
		Teo = 0
	return cat
print(addValuesInAllRows([ [1,2,3], [10,20,30], [100,200,300] ]))


def addValuesInAllCols(meow):
	cat = []
	Teo = 0
	for row in range(len(meow)):
		for column in range(len(meow[row])):
			Teo += meow[column][row]
		cat.append(Teo)
		Teo = 0
	return cat
print(addValuesInAllCols([ [1,2,3], [10,20,30], [100,200,300] ]))


def addUpperDiagonalMatrix(meow):
	Teo = 0
	for row in range(len(meow)):
		for column in range(len(meow[row]) - row):
			Teo += meow[row][column+row]
	return Teo
print(addUpperDiagonalMatrix([[1,2,3,4],[10,20,30,40],[100,200,300,400],[1000,2000,3000,4000]]))


def add10FromPosUntilPosInCol(mat, col, row1, row2):
	for row in range(row1, row2+1):
		mat[row][col] = mat[row][col] + 10
	return mat
mat = [[1,2,3,4,5],[10,20,30,40,50],[100,200,300,400,500]] 
print(add10FromPosUntilPosInCol(mat,3,0,2))


def IsSumAllValuesEven(meow):
	cat = 0
	for row in range(len(meow)):
		for column in range(len(meow[row])):
			cat += meow[row][column]
	if cat % 2 == 0:
		return True
	else:
		return False
print(IsSumAllValuesEven([[1,2,3],[10,20,30],[100,200,300]]))


def convert_2_to_10(meow):
	cat = 0
	meow.reverse()
	for i in range(len(meow)):
		if meow[i] == 1:
			cat += 2 ** i
	return cat
print(convert_2_to_10([1, 1, 1]))


def add10FromPosUntilPosInList(meow, pos1, pos2):
	for i in range(pos1, pos2+1):
		meow[i] = meow[i] + 10
	return meow
print(add10FromPosUntilPosInList([0,100,200,300,400,500], 1, 4))


def add10FromPosUntilPosInRow(meow, row, col1, col2):
	for column in range(col1, col2+1):
		meow[row][column] = meow[row][column] + 10
	return meow
mat = [[1,2,3,4,5],[10,20,30,40,50],[100,200,300,400,500]]
print(add10FromPosUntilPosInRow(mat, 2, 1, 3))