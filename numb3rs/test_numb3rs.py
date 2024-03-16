from numb3rs import validate

def main():
    test_len()
    test_name()
    test_nums()
    


def test_nums():
    assert validate("1.2.3.5") == True
    assert validate("275.65.89.0") == False

def test_name():
    assert validate("cat") == False
    assert validate("cat.5.6.7") == False

def test_len():
    assert validate("1.2.3") == False