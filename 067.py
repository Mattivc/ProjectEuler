"""
Project Euler Problem 67
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^99
altogether! If you could check one trillion (10^12) routes every second it
would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)
"""

triangle = []

with open('067_data.txt') as f:
	for line in f:
		line_array = []
		for n in line.split(' '):
			line_array.append(int(n))
		triangle.append(line_array)

rows = len(triangle)
memo = {}

def max_path_sum(row, element):
	if row >= rows: # we have moved past the last row
		return 0

	if (row, element) in memo:
		return memo[(row, element)]

	value = max(max_path_sum(row+1, element), max_path_sum(row+1, element+1)) + triangle[row][element]
	memo[(row, element)] = value
	return value

print max_path_sum(0,0)
