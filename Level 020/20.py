import math

def level20():
	return sum(map(int, str(math.factorial(100))))
	
if __name__ == "__main__":
	print level20()