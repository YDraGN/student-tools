import pytest

from src.calculator import (
    add,
    subtract,
    multiply,
    divide,
    validate_number,
)


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_validate_integer():
    assert validate_number(10) is True


def test_validate_float():
    assert validate_number(10.5) is True


def test_validate_string():
    with pytest.raises(ValueError, match="Input must be a number"):
        validate_number("abc")


def test_validate_none():
    with pytest.raises(ValueError, match="Input must be a number"):
        validate_number(None)