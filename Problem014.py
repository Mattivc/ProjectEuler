def Collatz(n):
	chain = 0

	while n > 1:
		if (n % 2 == 0):
			n = n/2
		else:
			n = 3*n + 1
		chain += 1
	return chain

largest_num = 0
largest_chain = 0

for i in range(0, 1000000):
	chain = Collatz(i)
	if (chain > largest_chain):
		largest_chain = chain
		largest_num = i


print(largest_num)
