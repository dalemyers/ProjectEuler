def get_abundant(maxVal):
	factors = [0]*maxVal
	abundant = []
	
	for i in range(1, maxVal):
		for j in range(i, maxVal, i):
			factors[j] += i
			
	for i in range(0, maxVal):
		factors[i] -= i
		if factors[i] > i:
			abundant.append(i)
			
	return abundant


def level23():
	maxVal = 28123 + 1

	abundant = get_abundant(maxVal)
	
	nonAbundantSum = 0
	abundantSum = {}

	for i in range(0, maxVal):
		abundantSum[i] = False
	
	for i in range(0,len(abundant)):
		for j in range(i, len(abundant)):
			if abundant[i] + abundant[j] > maxVal:
				break
			
			abundantSum[abundant[i] + abundant[j]] = True
	
	for i in range(0, maxVal):
		if not abundantSum[i]:
			nonAbundantSum += i
			
	return nonAbundantSum
	
if __name__ == "__main__":
	print level23()