def numToString(n):
	numbers = {	1:"one",
			2:"two",
			3:"three",
			4:"four",
			5:"five",
			6:"six",
			7:"seven",
			8:"eight",
			9:"nine",
			10:"ten",
			11:"eleven",
			12:"twelve",
			13:"thirteen",
			14:"fourteen",
			15:"fifteen",
			16:"sixteen",
			17:"seventeen",
			18:"eighteen",
			19:"nineteen",
			20:"twenty",
			30:"thirty",
			40:"forty",
			50:"fifty",
			60:"sixty",
			70:"seventy",
			80:"eighty",
			90:"ninety",
			100:"hundred"
			}
	
	if n == 1000:
		return "one thousand"
	
	if n >= 100:
		hundreds = int(n/100)
		if n % 100 == 0:
			return numToString(hundreds) + " hundred"
		else:
			return numToString(hundreds) + " hundred and " + numToString(n - 100*hundreds)
	
	if n >= 20:
		tens = int(n / 10)
		if n % 10 == 0:
			return numbers[n]
		else:
			return numbers[tens*10] + "-" + numbers[n - tens*10]
	
	return numbers[n]

def level17():
	total = 0
	for i in range(1,1001):
		total += len(numToString(i).replace(" ","").replace("-",""))
	return total
	
if __name__ == "__main__":
	print level17()