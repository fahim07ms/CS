import sys

def main():
	#Check argv
	check_arg()
	counter = 0
	try:
		with open(sys.argv[1]) as file:
			for line in file:
				#print(bool(line.isspace()))
				#print(line.splitlines())
				
				if line.isspace():
					continue
				elif line.strip().startswith('#'):
					continue
				else:
					counter += 1
	except FileNotFoundError:
		sys.exit("File Not Found")
	
	print(counter)
	
	
def check_arg():
	len_arg = len(sys.argv)
	if len_arg < 2:
		sys.exit("Too few command-line argument")
	elif len_arg > 2:
		sys.exit("Too many command-line arguments")
	else:
		if sys.argv[1][len(sys.argv[1])-3:len(sys.argv[1])] != ".py":
			sys.exit("Not a python file")
	
if __name__ == "__main__":
	main()