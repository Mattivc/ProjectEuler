
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

sum = 0

for i in range(2, 2000000):
	if(is_prime(i)):
		sum += i

print(sum)
