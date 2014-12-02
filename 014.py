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
