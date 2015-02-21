"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

cache = {1:1}

def Collatz(n):
	cache_value = cache.get(n, -1)
	if cache_value != -1:
		return cache_value

	if (n % 2 == 0):
		m = n/2
	else:
		m = 3*n + 1
	
	collatz_value_of_n = (Collatz(m) + 1)
	cache[n] = collatz_value_of_n
	return collatz_value_of_n

largest_num = 0
largest_chain = 0

for i in range(1, 1000000):
	chain = Collatz(i)
	if (chain > largest_chain):
		largest_chain = chain
		largest_num = i

print(largest_num)
