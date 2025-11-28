import operator

def level8():
	seq = ""
	length = 13
	max = -1
	with open("data.txt") as f:
		seq = f.readline()
	
	for i in range(0,len(seq) - length):
		s = reduce(operator.mul, map(int, seq[i:i+length]), 1)
		if s > max:
			max = s

	return max
	
if __name__ == "__main__":
	print level8()