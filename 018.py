"""
Project Euler Problem 18
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

NOTE: As there are only 16384 routes, it is possible to solve this problem
   by trying every route. However, Problem 67, is the same challenge with
a triangle containing one-hundred rows; it cannot be solved by brute
force, and requires a clever method! ;o)
"""

triangle = []

with open('018_data.txt') as f:
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
