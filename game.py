from random import randint

def main():
	num = randint(1, ask_lv())
	
	guess(num)
		
def ask_lv():
	while True:
		lv = int(input("Level: "))
		if lv > 0:
			return lv

def guess(num):
	while True:
		us_num = int(input("Guess: "))
	
		if us_num == num:
			 print("Just right!")
			 break;
		elif us_num > num:
			print("Too big!")
		else:
			print("Too small")
		
	
if __name__ == "__main__":
	main()