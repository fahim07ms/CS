import requests
import json
import sys

def main():
	n = get_num(sys.argv)
	
	responses = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
	
	rate = float(responses.json()["bpi"]["USD"]["rate"].replace(",", ""))
	print(f"${(rate*n):,.4f}")


# Read System
def get_num(arg):
	while True:
		if len(arg) == 1:
			sys.exit("Command-line argument is missing")
		elif len(arg) == 2:
			try:
				return float(arg[1])
			except ValueError:
				sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
	main()


#print(json.dumps(response.json(), indent=2))