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


@pytest.mark.parametrize("operation", [add, subtract, multiply, divide])
@pytest.mark.parametrize("invalid_value", ["abc", None, True])
def test_calculation_rejects_invalid_first_input(operation, invalid_value):
    with pytest.raises(ValueError, match="Input must be a number"):
        operation(invalid_value, 2)


@pytest.mark.parametrize("operation", [add, subtract, multiply, divide])
@pytest.mark.parametrize("invalid_value", ["abc", None, True])
def test_calculation_rejects_invalid_second_input(operation, invalid_value):
    with pytest.raises(ValueError, match="Input must be a number"):
        operation(2, invalid_value)


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


def test_validate_negative_integer():
    assert validate_number(-10) is True


def test_add_negative_numbers():
    assert add(-5, 3) == -2
    assert add(-5, -3) == -8


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2


def test_multiply_negative_numbers():
    assert multiply(-4, 3) == -12
    assert multiply(-4, -3) == 12


def test_divide_negative_numbers():
    assert divide(-10, 2) == -5
    assert divide(-10, -2) == 5
