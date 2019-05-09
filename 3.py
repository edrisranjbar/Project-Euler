from functools import reduce
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def isPrime(x):
	if x < 2 : return
	for y in range(2, int(x**0.5) + 1):
		if not (x % y):
			return False
	return True
factors = factors(600851475143)
primeFactors = []
for factor in factors:
    if isPrime(factor):
        primeFactors.append(factor)
print(max(primeFactors))
