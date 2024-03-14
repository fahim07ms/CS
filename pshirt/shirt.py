import sys
from   PIL import Image, ImageOps

def main():
    #Check arg
    check_arg();

    try:
        before = Image.open(sys.argv[1])
       
    except OSError:
        sys.exit("Invalid input")
    except FileNotFoundError:
    	sys.exit("File not found")
    	
    shirt = Image.open("shirt.png")
    
    crpd = ImageOps.fit(shirt, size=(before.size[0], shirt.size[1]))
    
    after = Image.new(mode=before.mode, size=before.size)
 
    after.paste(crpd)
    after.paste(before, box=(0, before.size[1]))
    
    after.save(sys.argv[2], format=before.format)

    


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
