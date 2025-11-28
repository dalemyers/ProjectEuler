def level9():
	for a in range(1,1000):
		for b in range(a,1000):
			if a + b > 999 or a**2 + b**2 > 1000000:
				break
			for c in range(1000 - (a + b),1000):
				if a + b + c > 1000:
					break
				if a**2 + b**2 == c**2 and a + b + c == 1000:
					return a*b*c
					
if __name__ == "__main__":
	print level9()