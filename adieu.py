names = [];

while True:
	try: 
		names.append(input("Name: "));
	except EOFError:
		text = "\nAudie ";
		ln = len(names);
		for i in range(ln):
			if ln == 1:
				text += f"{names[i]}";
			else:
				if i == (ln-1):
					text += f"and {names[i]}";
				else:
					text += f"{names[i]}, ";
		print(text);
		break;