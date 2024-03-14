from gauge import convert, gauge
from pytest import raises

def main():
    test_upbig()

def test_upbig():
    with raises(ValueError):
        convert('4/1')

def test_zero():
    with raises(ZeroDivisionError):
        convert('4/0')

def test_otherinput():
    with raises(ValueError):
        convert('cat/dog')

def test_upbig():
    with raises(ValueError):
        convert('4/1')

def test_e():
    assert gauge(convert('1/100')) == "E"

def test_f():
    assert gauge(convert("1/1")) == "F"

def test_other():
    assert gauge(convert("1/4")) == "25%"

main()
