def fib(maxValue):
	values = [1,1]
	while True:
		total = values[-1] + values[-2]
		if total > maxValue:
			break
		values.append(total)
	return values


def level2():
	return sum([x for x in fib(4000000) if x % 2 == 0])


if __name__ == "__main__":
	print level2()