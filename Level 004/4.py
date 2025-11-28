def is_palindrome(x):
	sx = str(x)
	return sx == sx[::-1]

def level4():
	palindromes = []
	for x in range(100,999):
		for y in range(x,999):
			if is_palindrome(x*y):
				palindromes.append(x*y)
	return max(palindromes)

if __name__ == "__main__":
	print level4()