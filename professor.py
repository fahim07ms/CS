from random import randrange

def main():
	n = get_level();
	
	score = 0;
	
	for i in range(10):
		num = get_integer(n)
		sum = num[0] + num[1]
		for i in range(3):
			try:
				us_num = int(input(f"{num[0]} + {num[1]} = "))
			except ValueError:
				pass;
				us_num = -1
			if us_num == sum:
				score += 1;
				break;
			else:
				print("EEE")
				if i == 2:
					print(f"{num[0]} + {num[1]} = {sum}")
					break;
					
	print(f"Score: {score}");
				
					
	
def get_level():
	while True:
		try:
			n = int(input("Level: "));
			break
		except ValueError:
			pass
	
	return n
	
def get_integer(n):
	return [randrange(0, 10**n), randrange(0, 10**n)]
	
if __name__ == "__main__":
	main();