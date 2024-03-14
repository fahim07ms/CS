import sys, csv

def main():
    #Check arg
    chech_arg()

    with open(sys.argv[1]) as rfile:
        reader = csv.DictReader(rfile)

        with open(sys.argv[2], "w", newline="") as wfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(wfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                last, first = row["name"].rsplit()

                writer.writerow({
                        "first": first,
                        "last": last.replace(",", ""),
                        "house": row["house"]
                    })


def chech_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command line argument")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line argument")
    elif sys.argv[1].endswith(".csv") == False or sys.argv[2].endswith(".csv") == False:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()