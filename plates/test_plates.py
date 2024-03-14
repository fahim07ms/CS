from plates import is_valid

def main():
    test_len()
    test_start()
    test_character()
    test_middle()
    test_zero()

def test_start():
    assert is_valid("AA20") == True
    assert is_valid("HELLO") == True
    assert is_valid("A20") == False
    assert is_valid("20AA") == False

def test_len():
    assert is_valid("CS") == True
    assert is_valid("A") == False
    assert is_valid("OUT4000") == False

def test_zero():
    assert is_valid("AA02") == False

def test_middle():
    assert is_valid("AA20CC") == False

def test_character():
    assert is_valid("AA.20") == False
    assert is_valid(".AA20") == False
    assert is_valid("AA20.") == False
    
    
    
    
    
    
    
    
    