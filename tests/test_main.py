from src.main import add
from src.main import subtract
def test_add_function():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(1, 5) == 6
    assert add(5, 0) == 5

def test_subtract_function():
    assert subtract(2, 2) == 0
    assert subtract(0, 0) == 0