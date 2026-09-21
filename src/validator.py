def validate_number(value):
    if isinstance(value, bool):
        raise ValueError("Input must be a number")
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")
    return True