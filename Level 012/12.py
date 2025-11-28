 	
def factors(x):
	divisors = 0
	for i in xrange(1, x/2 + 1):
		if x % i == 0:
			divisors += 1
	
	return divisors
		
def level12():
	max_divs = 0
	tn = 0
	i = 0
	while True:
		i += 1
		tn += i
		if i % 2 == 0:
			divisors = factors(i/2) * factors(i+1)
		else:
			divisors = factors(i) * factors((i+1)/2)
			
		if divisors > max_divs:
			max_divs = divisors
				
		if divisors > 500:
			return tn
		
		
if __name__ == "__main__":
	print level12()