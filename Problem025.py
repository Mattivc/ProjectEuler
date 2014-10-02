import math

def fibo_iter():
    n_1, n_2 = 1, 1
    while 1:
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2

length = 0
f = fibo_iter()
n = 0

while length < 1000:
	n += 1
	fibo = next(f)
	length = int(math.log10(fibo))+1

print n
