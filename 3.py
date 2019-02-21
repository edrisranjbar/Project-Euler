def factorsOf (number):
    factors = []
    for i in range(1,number+1):
        if number % i == 0 :
            factors.append(i)
    print ("Factors of {} is/are {}".format(number,factors))
    return factors

def isPrime(x):
	if x >= 2:
		for y in range(2, x):
			if not (x % y):
				return False
	else:
		return False
	return True

number = 600851475143
factors = factorsOf(number)
primeFactors = []
for factor in factors:
    if isPrime(factor):
        primeFactors.append(factor)
print("Prime factors are: " + str(primeFactors))
print(max(primeFactors))