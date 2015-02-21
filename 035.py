"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from itertools import permutations

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    
@memoize
def is_prime(n):
    if n < 2: # Any number below 2 is not a prime
            return False
    if n == 2: # 2 is a prime
            return True
    if n % 2 == 0: # Any even number above 2 is not a prime
            return False

    for x in range(3, int(n**0.5)+ 1, 2):
            if n % x == 0:
                    return False
    return True

answer = 0

def rotations(n):
	str_list = list(str(n))
	rot = []
	for i in range(len(str(n))):
		rot.append(int(''.join(str_list)))
		tmp = str_list.pop(0)
		str_list.append(tmp)
	return rot


for i in range(1000000):
	rots = rotations(i)
	for rot in rots:
		if not is_prime(rot):
			break
	else:
		answer += 1

print answer

