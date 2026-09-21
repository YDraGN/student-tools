import pytest
from src.validator import validate_number


def test_validate_integer():
    assert validate_number(10) is True


def test_validate_float():
    assert validate_number(10.5) is True


def test_validate_string():
    with pytest.raises(ValueError, match="Input must be a number"):
        validate_number("abc")


def test_validate_bool():
    with pytest.raises(ValueError, match="Input must be a number"):
        validate_number(True)