def level6():
	sumsquare = sum([x**2 for x in range(1,101)])
	squaresum = sum(range(1,100))**2
	return squaresum - sumsquare

if __name__ == "__main__":
	print level6()