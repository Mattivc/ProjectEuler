def sum_of_squares(n):
	sum = 0
	for x in range(1,n+1):
		sum += x*x
	return sum

def square_of_sum(n):
	sum = 0
	for x in range(1,n+1):
		sum += x
	sum *= sum
	return sum

print(square_of_sum(100) - sum_of_squares(100))