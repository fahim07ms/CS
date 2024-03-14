from bank import value

def main():
    test_hello();
    test_h();
    test_other();


def test_hello():
    assert value("hello") == 0
    assert value("hello, world") == 0
    assert value("  hello, fahim ") == 0
    assert value("  Hello, Fahim ") == 0

def test_h():
    assert value("  hey ") == 20
    assert value(" Hey, fahim") == 20
    assert value(" HOW ARE YOU?") == 20

def test_other():
    assert value("what's up?") == 100
    assert value("GOOD MORNING") == 100