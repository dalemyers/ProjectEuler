def collatz(n):
	if n % 2 == 0:
		return n/2
	else:
		return 3*n + 1
		
def collatz_seq(n, stored_results):
	if n == 1:
		return [1]
		
	try:
		return stored_results[n]
	except KeyError:
		pass
		
	result = [n] + collatz_seq(collatz(n),stored_results)
	stored_results[n] = result
	return result
		
def level14():
	maxLen = 0
	num = 0
	stored_results = {}
	for i in range(500001,1000000,2):
		s = collatz_seq(i,stored_results)
		if len(s) > maxLen:
			maxLen = len(s)
			num = i
		print i
	return num
		
		
if __name__ == "__main__":
	print level14()