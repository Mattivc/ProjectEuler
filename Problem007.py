def is_prime(n):
	if(n < 2):
		return False

	for x in range(2,n):
		if(n % x == 0):
			return False
	return True

p = 0
n = 2

while True:
	if (is_prime(n)):
		p += 1
	if(p >= 10001):
		print(n)
		break
	n += 1
