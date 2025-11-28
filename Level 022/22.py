def get_data():
	with open("data.txt") as f:
		line = f.readlines()[0]
	
	names = line.split(",")
	names = map(lambda x : x.replace('"',''), names)
	return names
	
def name_value(name):
	return sum(map(lambda x : x - ord('A') + 1, map(ord,name)))

def level22():
	names = get_data()
	names.sort()
	nvtotal = 0
	for i in range(0,len(names)):
		nvtotal += name_value(names[i]) * (i+1)
		
	return nvtotal
	
	
if __name__ == "__main__":
	print level22()