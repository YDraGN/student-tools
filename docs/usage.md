# Hướng dẫn sử dụng (Usage Guide)

Tài liệu hướng dẫn chi tiết cách sử dụng các module và hàm tiện ích trong gói công cụ `student-tools`.

---

## 1. Temperature Converter (`src/converter.py`)

Module `converter.py` cung cấp các hàm hỗ trợ chuyển đổi qua lại giữa hai thang đo nhiệt độ phổ biến: **Celsius (°C)** và **Fahrenheit (°F)**.

### 1.1. Công thức toán học
- **Celsius sang Fahrenheit:**
  $$\text{°F} = \text{°C} \times \frac{9}{5} + 32$$
- **Fahrenheit sang Celsius:**
  $$\text{°C} = (\text{°F} - 32) \times \frac{5}{9}$$

---

### 1.2. Danh sách các hàm

#### `celsius_to_fahrenheit(celsius)`
Chuyển đổi nhiệt độ từ Celsius (°C) sang Fahrenheit (°F).

- **Tham số:**
  - `celsius` (`float` hoặc `int`): Giá trị nhiệt độ theo độ C.
- **Giá trị trả về:**
  - `float`: Giá trị nhiệt độ tương ứng theo độ F.
- **Ví dụ sử dụng:**
  ```python
  from src.converter import celsius_to_fahrenheit

  print(celsius_to_fahrenheit(0))      # 32.0 (Nước đóng băng)
  print(celsius_to_fahrenheit(37))     # 98.6 (Thân nhiệt người)
  print(celsius_to_fahrenheit(100))    # 212.0 (Nước sôi)
  print(celsius_to_fahrenheit(-40))    # -40.0 (Điểm giao nhau)
  ```

#### `fahrenheit_to_celsius(fahrenheit)`
Chuyển đổi nhiệt độ từ Fahrenheit (°F) sang Celsius (°C).

- **Tham số:**
  - `fahrenheit` (`float` hoặc `int`): Giá trị nhiệt độ theo độ F.
- **Giá trị trả về:**
  - `float`: Giá trị nhiệt độ tương ứng theo độ C.
- **Ví dụ sử dụng:**
  ```python
  from src.converter import fahrenheit_to_celsius

  print(fahrenheit_to_celsius(32))     # 0.0 (Nước đóng băng)
  print(fahrenheit_to_celsius(98.6))   # 37.0 (Thân nhiệt người)
  print(fahrenheit_to_celsius(212))    # 100.0 (Nước sôi)
  print(fahrenheit_to_celsius(-40))    # -40.0 (Điểm giao nhau)
  ```

---

### 1.3. Bảng mốc nhiệt độ tham chiếu

| Trạng thái / Mốc nhiệt độ | Độ Celsius (°C) | Độ Fahrenheit (°F) |
| :--- | :---: | :---: |
| Không độ tuyệt đối (Absolute Zero) | -273.15 | -459.67 |
| Điểm giao thoa giữa hai thang đo | -40.0 | -40.0 |
| Nước đóng băng (Freezing point) | 0.0 | 32.0 |
| Nhiệt độ phòng tiêu chuẩn (Room temp) | 25.0 | 77.0 |
| Thân nhiệt người bình thường | 37.0 | 98.6 |
| Nước sôi ở áp suất tiêu chuẩn (Boiling point) | 100.0 | 212.0 |

---

### 1.4. Lưu ý khi sử dụng
- Các hàm chấp nhận cả kiểu số nguyên (`int`) và số thực (`float`), hỗ trợ đầy đủ cả số âm và số dương.
- Kết quả trả về luôn là số thực (`float`) để đảm bảo độ chính xác phép tính.

---

## 2. Validator (`src/validator.py`)

Module `validator.py` cung cấp hàm `validate_number(value)` để kiểm tra tính hợp lệ của dữ liệu số đầu vào trước khi thực hiện các phép toán.

- **Đầu vào hợp lệ:** kiểu `int` hoặc `float`.
- **Ngoại lệ:** Ném ra `ValueError("Input must be a number")` nếu giá trị đầu vào là kiểu `str`, `None`, hoặc `bool`.
