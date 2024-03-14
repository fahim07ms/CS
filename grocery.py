grocery = {}

while True:
	try:
		item = input("").upper();
		if item in grocery:
			grocery[item] += 1;
		else:
			grocery[item] = 1;
	except EOFError:
		lists = sorted(list(grocery))
		for i in lists:
			print(f"{grocery[i] } {i}")
		break;
		