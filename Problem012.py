from sets import Set

def sum_to_n(n):
    return (n*(n+1))/2

def quickFactor(n):
    return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))


i = 1
max = 0

while 1:
    n = sum_to_n(i)
    factors = quickFactor(n)
    if factors > max:
        max = factors

    if factors > 500:
        print n
        break
    i += 1

