## Temperature Converter

Module `converter.py` cung cấp các hàm chuyển đổi nhiệt độ giữa hai đơn vị Celsius và Fahrenheit.

### Các hàm

#### `celsius_to_fahrenheit(celsius)`
Chuyển đổi nhiệt độ từ Celsius (°C) sang Fahrenheit (°F).

**Tham số:**
- `celsius` (float): Nhiệt độ theo độ C.

**Trả về:** Nhiệt độ theo độ F (float).

**Ví dụ:**
```python
from src.converter import celsius_to_fahrenheit

print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
```

#### `fahrenheit_to_celsius(fahrenheit)`
Chuyển đổi nhiệt độ từ Fahrenheit (°F) sang Celsius (°C).

**Tham số:**
- `fahrenheit` (float): Nhiệt độ theo độ F.

**Trả về:** Nhiệt độ theo độ C (float).

**Ví dụ:**
```python
from src.converter import fahrenheit_to_celsius

print(fahrenheit_to_celsius(32))   # 0.0
print(fahrenheit_to_celsius(212))  # 100.0
```

## Validator

Module `validator.py` cung cấp hàm `validate_number(value)` để kiểm tra
đầu vào có phải là số hợp lệ (int/float) hay không. Ném ra `ValueError`
nếu input là chuỗi, None, hoặc boolean.