import sys
from datetime import date
from validator_collection import validators
from inflect import engine

def main():
    td = date.today()

    birth = date_validator(input("Date of birth: ").strip())

    word = engine().number_to_words(((td-birth).days*24*60), comma=None,andword=", ").capitalize()

    new_word = word.replace(",", "", (word.count(",")-1))

    print(new_word , "minutes")

def date_validator(s):
    try:
        return validators.date(date.fromisoformat(s))
    except Exception:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()