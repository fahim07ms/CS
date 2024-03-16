import sys
from   PIL import Image, ImageOps

def main():
    #Check arg
    check_arg();

    #Trying to open image unless File Not Found or Invalid Input
    try:
        before = Image.open(sys.argv[1]) 
    except OSError:
        sys.exit("Invalid input")
    except FileNotFoundError:
        sys.exit("File not found")
    
    # Opening the shirt
    shirt = Image.open("shirt.png")

    # Cropping the bigger user image
    crpd = ImageOps.fit(before, (shirt.size[0], shirt.size[1]))
    
    # Pasting the shirt in cropped image
    crpd.paste(shirt, mask=shirt)
    crpd = crpd.convert('RGB')

    crpd.save(sys.argv[2], format=before.format)


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
