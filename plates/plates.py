def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s_len = len(s)
    if s_len < 2 or s_len > 6:
        return False
    if s.isalnum() == False:
        return False
    if s[0:2].isalpha() == False:
        return False
    has_num = any(chr.isdigit() for chr in s)
    if has_num and s[s_len-1:s_len].isalpha():
        return False;
    try:
        if s[s.index('0')-1].isalpha():
            return False
    except ValueError:
        pass

    return True

if __name__ == "__main__":
    main()