import math

def level15():
	x = 20
	y = 20
	return math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
	
if __name__ == "__main__":
	print level15()