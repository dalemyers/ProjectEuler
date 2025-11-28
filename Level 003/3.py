from math import *
import operator

def level3():
	num = 600851475143
	maxValue = num
	counter = 3
	known_primes = [2]
	factors = []
	while counter < sqrt(maxValue):
		isPrime = True
		for i in known_primes:
			if counter % i == 0:
				isPrime = False
				counter += 2
		if isPrime:
			known_primes.append(counter)
			if maxValue % counter == 0:
				factors.append(counter)
				maxValue /= counter
				
	return num / reduce(operator.mul,factors,1)
	

if __name__ == "__main__":
	print level3()