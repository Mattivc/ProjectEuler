
def is_prime(n):
	if(n < 2):
		return False

	for x in range(2,n):
		if(n % x == 0):
			return False
	return True

def factorize(n):
	factors = []

	f = 2
	while is_prime(n) == False:
		if(n % f == 0):
			factors.append(f)
			n = int(n/f)
			f = 2
		f += 1

	factors.append(n)
	return factors
		

print(max(factorize(600851475143)))
