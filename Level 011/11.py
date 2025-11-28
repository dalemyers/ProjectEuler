import math

def get_data():
	with open('data.txt') as f:
		textlines = f.readlines();
	lines = []
	for textline in textlines:
		textnums = textline.replace("\n", "").split(" ")
		textnums = map(int, textnums) + [1,1,1]
		lines.append(textnums)
	
	lines.append([1]*23)
	lines.append([1]*23)
	lines.append([1]*23)
	
	return lines

def level11():
	grid = get_data()
	maxP = 0
	for x in range(0, 20 - 3): #Don't check final 4
		for y in range(0, 20 - 3):
			if grid[x][y] * grid[x+1][y] * grid[x+2][y] * grid[x+3][y] > maxP:
				maxP = grid[x][y] * grid[x+1][y] * grid[x+2][y] * grid[x+3][y]
				
			if grid[x][y] * grid[x+1][y+1] * grid[x+2][y+2] * grid[x+3][y+3] > maxP:
				maxP = grid[x][y] * grid[x+1][y+1] * grid[x+2][y+2] * grid[x+3][y+3]
			
			if grid[x][y+3] * grid[x+1][y+2] * grid[x+2][y+1] * grid[x+3][y] > maxP:
				maxP = grid[x][y+3] * grid[x+1][y+2] * grid[x+2][y+1] * grid[x+3][y]
			
			if grid[x][y] * grid[x][y+1] * grid[x][y+2] * grid[x][y+3] > maxP:
				maxP = grid[x][y] * grid[x][y+1] * grid[x][y+2] * grid[x][y+3]
			   
	return maxP
	
if __name__ == "__main__":
	print level11()