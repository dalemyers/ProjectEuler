def get_data():
	with open("data.txt") as f:
		strlines = f.readlines()
	
	triangle = []
	for strline in strlines:
		triangle.append([int(x) for x in strline.split()])
	
	return triangle

def level18():
	triangle = get_data()
	for y in range(len(triangle)-1,0,-1):
		for x in range(0, len(triangle[y]) - 1):
			a = triangle[y][x]
			b = triangle[y][x+1]
			triangle[y-1][x] = triangle[y-1][x] + max(a,b)
	
	return triangle[0][0]
	
if __name__ == "__main__":
	print level18()