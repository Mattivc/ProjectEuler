"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""

sum = 2
a = 1
b = 2
fib = 0

while fib < 4000000:
	fib = a + b
	a = b
	b = fib
	if (fib % 2 == 0):
		sum += fib
	

print(sum)
