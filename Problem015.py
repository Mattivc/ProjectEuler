dataCache = { (0,0): 1 }

def get_path_number(x, y):
	val = dataCache.get((x,y), -1) # try to get data from cache

	if (val == -1): # calculate the data if not found in cache
		if (x < 0):
			val = 0
		elif (y < 0):
			val = 0
		else:
			val = get_path_number(x-1,y) + get_path_number(x, y-1)
		dataCache.update({(x,y):val}) # add the data to cache
	return val

print(get_path_number(20,20))
