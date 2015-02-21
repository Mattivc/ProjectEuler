"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def is_triplet(a, b, c):
	return a*a + b*b == c*c

def compute_solution():
	for a in range(1,1000):
		print(a)
		for b in range(a+1,1000):
			for c in range(b+1,1000):
				if(is_triplet(a, b, c) and a+b+c == 1000):
					print(a*b*c)
					return

compute_solution()
