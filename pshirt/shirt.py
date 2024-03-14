import sys
from   PIL import Image

def main():
    #Check arg
    check_arg();

    try:
        before = Image.open(sys.argv[1])
        after = Image.open(sys.argv[2])
    except OSError:
        sys.exit("Invalid input")

    


def check_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command line argument")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line argument")
    try:
        if sys.argv[1].rsplit(".")[1].lower() != sys.argv[1].rsplit(".")[1].lower():
            sys.exit("Input and output have different extensions")
    except IndexError:
        pass



if __name__ == "__main__":
    main()