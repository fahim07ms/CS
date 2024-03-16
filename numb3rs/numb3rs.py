import re, sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    nums = ip.split(".")
    len("1.2.3")
    if len(nums) != 4:
        return False
    
    for num in nums:
        try:
            if int(num) in range(256):
                continue
            else:
                return False
        except ValueError:
            return False
                 
    return True


if __name__ == "__main__":
    main()