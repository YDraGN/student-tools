"""Module cung cấp các tiện ích chuyển đổi đơn vị trong student-tools.

Hiện tại hỗ trợ chuyển đổi nhiệt độ giữa hai thang đo Celsius (°C) và Fahrenheit (°F).
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Chuyển đổi nhiệt độ từ thang đo Celsius (°C) sang Fahrenheit (°F).

    Công thức: F = C * 9/5 + 32

    Args:
        celsius (float | int): Giá trị nhiệt độ theo độ Celsius.

    Returns:
        float: Giá trị nhiệt độ tương ứng theo độ Fahrenheit.

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
        >>> celsius_to_fahrenheit(-40)
        -40.0
    """
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Chuyển đổi nhiệt độ từ thang đo Fahrenheit (°F) sang Celsius (°C).

    Công thức: C = (F - 32) * 5/9

    Args:
        fahrenheit (float | int): Giá trị nhiệt độ theo độ Fahrenheit.

    Returns:
        float: Giá trị nhiệt độ tương ứng theo độ Celsius.

    Examples:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
        >>> fahrenheit_to_celsius(-40)
        -40.0
    """
    return (fahrenheit - 32) * 5 / 9
