
from addition import calculate_add

def test_calculate_position():
    assert calculate_add(10,20) == 30

def test_calculate_zero():
    assert calculate_add(10,0) == 10

def test_calculate_negative():
    assert calculate_add(-10,20) == 10