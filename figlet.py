import pyfiglet, sys
from random import randrange

fonts = pyfiglet.FigletFont.getFonts()

len_v = len(sys.argv)

if len_v == 1:
    f = pyfiglet.Figlet(font=fonts[randrange(0, len(fonts))])
    inp = input("Input: ")
    print(f.renderText(inp))
elif len_v == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            f = pyfiglet.Figlet(font=sys.argv[2])
            inp = input("Input: ")
            print(f.renderText(inp))
        except Exception:
            sys.exit()
    else:
        sys.exit()
    
    
    

