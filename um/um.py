import re, sys

def main():
    print(count(input("Text: ").strip()))

def count(s):
    match = re.findall("(?:\\b)(um)(?:\\b)", s, re.IGNORECASE)
    return len(match)


if __name__ == "__main__":
    main()