from math import factorial

# paths = (x + Y)! / (x! * y!)
def get_path_number(x, y):
	return factorial(x + y) / (factorial(x) * factorial(y))

print(get_path_number(20,20))
