import pytest
from app import add, subtract

def test_add():
    assert add(-1, 0) == -1

def test_subtract():
    assert subtract(9, 3) == 6
    assert subtract(5, 3) == 2
