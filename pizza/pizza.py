import sys, csv
from tabulate import tabulate

def main():
	#Check file
	check_arg()
	
	#Openig file
	try:
		with open(sys.argv[1]) as file:
			reader = csv.DictReader(file)
			
			
			print(tabulate(reader, headers="keys", tablefmt="grid"))
			
	except FileNotFoundError:
		sys.exit("No such file")
		
	
	
	
def check_arg():
	if len(sys.argv) < 2:
		sys.exit("Too few command-line argument")
	elif len(sys.argv) > 2:
		sys.exit("Too many command-line argument")
	elif sys.argv[1].endswith(".csv") == False:
		sys.exit("Not a CSV file")
	
	
if __name__ == "__main__":
	main()