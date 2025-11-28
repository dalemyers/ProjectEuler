def get_data():
	with open('data.txt') as f:
		strlines = f.readlines()
	lines = map(int,strlines)
	return lines
	
def level13():
	total = sum(get_data())
	return str(total)[:10]		
		
if __name__ == "__main__":
	print level13()