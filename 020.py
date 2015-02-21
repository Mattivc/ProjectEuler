"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""

factorial = 1
for n in range(2, 100):
    factorial *= n

digitsum = 0
for i in range(1,len(str(factorial))+1):
    digitsum += (factorial % 10**i)/ 10**(i-1)

print digitsum

