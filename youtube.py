import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search("https?://(?:www.)?youtube.com/embed/[^\"\' ]+", s):
        sub = re.sub("(www.)?youtube.com/embed", "youtu.be", matches.group(0))
    else:
        sub = None
    
    return sub

if __name__ == "__main__":
    main()