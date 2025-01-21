import pytest
from main import add

def test_add_not_implemented():
    with pytest.raises(NotImplementedError):
        add(1, 2)

def test_add_negative_numbers():
    with pytest.raises(NotImplementedError):
        add(-1, -2)

def test_add_mixed_numbers():
    with pytest.raises(NotImplementedError):
        add(1.5, -2.5)

def test_add_zero():
    with pytest.raises(NotImplementedError):
        add(0, 0)