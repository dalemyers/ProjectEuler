def is_prime(primes, p):

	#Check if it is already known to be prime
	if p in primes:
		return True
	
	#If it divides by any of our known primes then we know that it is not prime
	for prime in primes:
		#If we are past half way it's not
		if prime > p/2:
			return False
		
		#If it divides, it's not
		if p % prime == 0:
			return False

	#Now calculate all primes up to this value/2 from the last prime
	for i in range(primes[-1]+1, p/2):
		is_prime = True
		for j in primes:
			if j > i/2:
				break
			if i % j == 0:
				is_prime = False
				break
				
		if is_prime:
			primes.append(i)
	
	#now check again to see if we are prime
	for prime in primes:
		if p % prime == 0:
			return False
		
	return True

def level27():
	primes = [2,3,5,7,11,13,17,19] #Starting value to speed things up

	maxCount = 0
	pair = None
	
	for a in range(-1000,1000):
		#print a
		for b in range(-1000,1000):
			n = 0
			count = 0
			while True:
				if is_prime(primes, n**2 + a*n + b):
					count += 1
					if count > maxCount:
						maxCount = count
						pair = (a,b)
					print a,b,n
				else:
					break
				n += 1
			
	print pair,maxCount
	print primes
	return pair[0]*pair[1]
	
if __name__ == "__main__":
	print level27()