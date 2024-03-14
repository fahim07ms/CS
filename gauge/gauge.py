def main():
    while True: 
        try: 
            frac = input("Fraction: ")
            percentage = convert(frac)
            break;
        except ZeroDivisionError: pass
        except ValueError: pass
    print(gauge(percentage))
    


def convert(fraction):
    frac = fraction.split("/")
    up = int(frac[0])
    down = int(frac[1])
    if down == 0:
        raise ZeroDivisionError
    if up > down:
        raise ValueError
    return round((up/down)*100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()





"""def main():
    result = get_percentage('Fraction: ');
    print(f"{result}");

def get_percentage(prompt):
    while True: 
        try: 
            frac = input(prompt)
            up = int(frac[0])
            down = int(frac[2])
            res = round((up/down)*100)
        except ZeroDivisionError: pass
        except ValueError: pass
        else: 
            if res <= 1:
                return "E"
            elif res >= 99:
                return "F"
            else:
                return f"{res}%"

main();"""