
def is_triplet(a, b, c):
	return a*a + b*b == c*c

def compute_solution():
	for a in range(1,1000):
		print(a)
		for b in range(a+1,1000):
			for c in range(b+1,1000):
				if(is_triplet(a, b, c) and a+b+c == 1000):
					print(a*b*c)
					return

compute_solution()
