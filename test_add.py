from main import add

def test_add_positive_numbers():
    assert add(1, 2) == 3

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_add_mixed_numbers():
    assert add(1.5, -2.5) == -1.0

def test_add_zero():
    assert add(0, 0) == 0