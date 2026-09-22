def add(a, b):
    validate_number(a)
    validate_number(b)
    return a + b


def subtract(a, b):
    validate_number(a)
    validate_number(b)
    return a - b


def multiply(a, b):
    validate_number(a)
    validate_number(b)
    return a * b


def divide(a, b):
    validate_number(a)
    validate_number(b)

    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


def validate_number(value):
    if isinstance(value, bool):
        raise ValueError("Input must be a number")

    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")

    return True
