"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

from math import sqrt
from collections import defaultdict

prime_memo = {}
def is_prime(n):
	if n in prime_memo:
		return prime_memo[n]

	if(n < 2):
		prime_memo[n] = False
		return False

	for x in range(2,int(sqrt(n))+1):
		if(n % x == 0):
			prime_memo[n] = False
			return False
	prime_memo[n] = True
	return True

def factorize(n):
	factors = defaultdict(int)
	divisor = 2
	while not is_prime(n):
		if (n % divisor == 0):
			factors[divisor] += 1
			n /= divisor
			divisor = 2
		else:
			divisor += 1
	factors[n] += 1
	return factors

answer_factors = defaultdict(int)

for i in range(2, 21):
	i_factors = factorize(i)
	for key, value in i_factors.items():
		if value > answer_factors[key]:
			answer_factors[key] = value

answer = 1

for key, value in answer_factors.items():
	answer *= key**value

print answer

