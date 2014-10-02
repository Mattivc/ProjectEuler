targetVal = 999

def SumDivisibleBy(n):
	p = int(targetVal / n)
	sum = n*(p*(p+1)) / 2 # 1+2+3+...+n=1/2*n*(n+1)
	return int(sum)

print(SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15))
