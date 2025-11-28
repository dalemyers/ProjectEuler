def d(n):
	total = 0
	for i in xrange(1, n/2 + 1):
		if n % i == 0:
			total += i
	
	return total

def level21():
	sum = 0
	for n in range(1, 10000):
		x = d(n)
		if d(x) == n and n != x:
			sum += n
			
	return sum
	
if __name__ == "__main__":
	print level21()