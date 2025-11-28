def get_primes(maxVal):
	l = [True]*maxVal
	l[0] = False
	l[1] = False
	for i in range(2,maxVal):
		for j in range(2*i,maxVal,i):
			l[j] = False
	
	for i in range(2,len(l)):
		if l[i]:
			yield i

def get_cycle(n):
	l = []
	power = 10
	remainder = 0
	decs = ""
	while len(decs) < 2000: #Twice the length of the highest number
		remainder = (power + remainder) % n
		v = power / n
		decs = str(v % power)
		power *= 10
		remainder *= power
		
		if len(decs) % 2 == 0:
			if decs[:len(decs)/2] == decs[len(decs)/2:]:
				return decs[:len(decs)/2]
		
	return []

def level26():
	maxLen = 0
	maxVal = 0
	
	for i in get_primes(1000):
		cycle = get_cycle(i)
		cycleLen = len(cycle)
		if cycleLen > maxLen:
			maxLen = cycleLen
			maxVal = i
	
	return maxVal
	
if __name__ == "__main__":
	print level26()