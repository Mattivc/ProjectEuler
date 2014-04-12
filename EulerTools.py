
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
