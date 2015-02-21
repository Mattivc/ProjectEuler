"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

targetVal = 999

def SumDivisibleBy(n):
	p = int(targetVal / n)
	sum = n*(p*(p+1)) / 2 # 1+2+3+...+n=1/2*n*(n+1)
	return int(sum)

print(SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15))
