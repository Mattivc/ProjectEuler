def is_palindrome(n):
	narray = []
	while n > 0:
		narray.append(n % 10)
		n = int(n/10)

	length = len(narray)
	hlength =int(length/2)
	a = 0
	b = 0

	for x in range(0,hlength):
		if (narray[x] != narray[length-x-1]):
			return False
	return True

solution = 0

for x in reversed(range(100, 1000)):
	for y in reversed(range(100, x+1)):
		n = x*y
		if(n > solution and is_palindrome(n)):
			solution = n 

print(solution)
