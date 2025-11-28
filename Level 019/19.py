import datetime

def level19():
	d = datetime.datetime.strptime("01/01/1901",  "%m/%d/%Y")
	sunday_count = 0
	while str(d) != "2000-12-31 00:00:00":
		d += datetime.timedelta(days=1)
		if d.weekday() == 6 and d.day == 1:
			sunday_count += 1
	return sunday_count
	
	
	
if __name__ == "__main__":
	print level19()