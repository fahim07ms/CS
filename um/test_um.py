from um import count

def main():
    test_front_um()
    test_back_um()
    test_mid_um()
    test_many_um()
    test_word_um()
    test_mis_um()


def test_front_um():
    assert count("um") == 1
    assert count("um, how are you?") == 1

def test_back_um():
    assert count("hello, um") == 1
    assert count("will do that, um?") == 1
    assert count("I need to think, Um...") == 1


def test_mid_um():
    assert count("hello, um, world") == 1
    assert count("hello,um, world") == 1

def test_many_um():
    assert count("Um, thanks, um...") == 2
    assert count("Um, hello, um, world, um") == 3


def test_word_um():
    assert count("Yummy") == 0
    assert count("humble") == 0

def test_mis_um():
    assert count("um!") == 1
    assert count("um?") == 1
    assert count("um...um...") == 2


if __name__ == "__main__":
    main()