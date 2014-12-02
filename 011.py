from numpy import loadtxt
import os
path = os.path.dirname(__file__)
data = loadtxt(os.path.join(path,"011_data.txt"), delimiter=' ')

directions = [[0,1],[1,1],[1,0],[1,-1]]

def get_line(xPos, yPos, direction):
	n = 1
	for i in range(0,4):
		x = xPos+direction[1]*i
		y = yPos+direction[0]*i
		n *= data[y][x]
	return n

def get_grid(xStart, yStart, width, heigth, direction):
	n = 0
	for x in range(xStart, width):
		for y in range(yStart, heigth):
			n = max(n, get_line(x, y, direction))
	return n


sum = 0
sum = max(sum, get_grid(0, 0, 17, 20, directions[0]))
sum = max(sum, get_grid(0, 0, 17, 17, directions[1]))
sum = max(sum, get_grid(0, 0, 20, 17, directions[2]))
sum = max(sum, get_grid(3, 0, 20, 17, directions[3]))

print(int(sum))
