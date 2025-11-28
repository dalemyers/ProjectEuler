def fib():
	a = 1
	b = 1
	yield a
	yield b
	while True:
		a,b = b,a
		b += a
		yield b

def level25():
	counter = 0
	for i in fib():
		counter += 1
		if len(str(i)) >= 1000:
			return counter
	
if __name__ == "__main__":
	print level25()