def level7():
	primes = [2]
	i = 3
	while True:
		isPrime = True
		for p in primes:
			if i%p == 0:
				isPrime = False
				break
		if isPrime:
			primes.append(i)
		if len(primes) >= 10001:
			return primes[-1]
		i += 1

if __name__ == "__main__":
	print level7()