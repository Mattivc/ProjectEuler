def divisible(n):
	for x in range(1,21):
		if(n % x != 0):
			return False
	return True

n = 1

while True:
	if(divisible(n)):
		print(n)
		break
	else:
		n+=1
