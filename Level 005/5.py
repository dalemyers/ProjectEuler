import operator

def level5():
	checks = range(11,21)
	i = 1
	while True:
		divides = True
		for j in checks:
			if i % j != 0:
				divides = False
				break
		if divides:
			return i
		i += 1

if __name__ == "__main__":
	print level5()