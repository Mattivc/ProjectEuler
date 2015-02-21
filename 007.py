"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

from math import sqrt

def is_prime(n):
	if(n < 2):
		return False

	for x in range(2,int(sqrt(n))+1):
		if(n % x == 0):
			return False
	return True

p = 0
n = 2

while True:
	if (is_prime(n)):
		p += 1
	if(p >= 10001):
		print(n)
		break
	n += 1
