from cookies import Jar
from pytest import raises

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

def test_init():
    jar = Jar()
    assert jar.capacity == 12  
    
    jar = Jar(15)
    assert jar.capacity == 15

    with raises(ValueError):
        jar = Jar(-5)


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(3)

    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    assert jar.size == 0

    jar.deposit(12)
    assert jar.size == 12

    with raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar()
    with raises(ValueError):
        jar.withdraw(1)

    jar.deposit(8)
    jar.withdraw(3)

    assert jar.size == 5
    