"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def d(n):
	total = 0
	for i in range(1,(n/2)+1):
		if n % i == 0:
			total += i
	return total

def amicable(n):
	d_n = d(n)
	return d(d_n) == n

answer = 0

for i in range(10000):
	if amicable(i):
		answer += i

print answer

