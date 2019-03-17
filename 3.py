def factorsOf (number):
    factors = []
    for i in range(1,number//2):
        if number % i == 0 :
            factors.append(i)
    factors.append(number)
    return factors
def isPrime(x):
	if x < 2 : return
	for y in range(2, int(x**0.5) + 1):
		if not (x % y):
			return False
	return True
factors = factorsOf(60085143)
primeFactors = []
for factor in factors:
    if isPrime(factor):
        primeFactors.append(factor)
print(max(primeFactors))
