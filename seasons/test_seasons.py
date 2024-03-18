from seasons import date_validator
from pytest import raises

def main():
    test_invalid_input()


def test_invalid_input():
    with raises(SystemExit):
        date_validator("January 1, 2020")
    with raises(SystemExit):
        date_validator("19 March 2020")
    with raises(SystemExit):
        date_validator("1/2/2020")
    with raises(SystemExit):
        date_validator("2020/08/08")
    