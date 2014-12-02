from math import factorial

# Combinatorial solution
# paths = (x + Y)! / (x! * y!)
def get_path_number_combinatorial(x, y):
	return factorial(x + y) / (factorial(x) * factorial(y))

print(get_path_number_combinatorial(20,20))

# Recursive solution with caching
dataCache = { (0,0): 1 }
def get_path_number_recursion(x, y):
	val = dataCache.get((x,y), -1) # try to get data from cache

	if (val == -1): # calculate the data if not found in cache
		if (x < 0):
			val = 0
		elif (y < 0):
			val = 0
		else:
			val = get_path_number_recursion(x-1,y) + get_path_number_recursion(x, y-1)
		dataCache.update({(x,y):val}) # add the data to cache
	return val

print(get_path_number_recursion(20,20))
