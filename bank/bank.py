def main():
    greet = input("Greeting: ");

    print(f"${value(greet)}")



def value(greeting):
    new_greet = greeting.strip().lower();
    first_word = new_greet.split(' ')[0].split(',')[0]
    if first_word == "hello":
        return 0;
    elif first_word[0] == "h":
        return 20;
    else: 
        return 100;


if __name__ == "__main__":
    main()