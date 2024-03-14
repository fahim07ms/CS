def main():
	text = input("Text: ")
	print(shorten(text))

def shorten(str):
	for letter in str:
		l = letter.lower()
		if l == 'a' or l == 'i' or l == 'e' or l == 'o' or l == 'u':
			str = str.replace(letter, "")
	return str
	
if __name__ == "__main__":
	main()