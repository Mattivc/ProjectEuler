
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