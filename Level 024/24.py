import itertools

def level24():
	chars = "0123456789"
	perms = itertools.permutations(chars)
	perms = list(perms)
	perms.sort()
	return "".join(perms[1000000-1])
	
if __name__ == "__main__":
	print level24()