def decimal_to_binary(n):
    stack = []  # สร้าง Stack
    # หากเลข n เป็น 0, ก็คืนค่าผลลัพธ์เป็น "0"
    if n == 0:
        return "0"
    while n > 0:
        stack.append(n % 2)  # เก็บเศษจากการหาร 2
        n = n // 2  # หาร n ด้วย 2   
    binary = ""
    while stack:
        binary += str(stack.pop())  # นำตัวเลขใน Stack มาต่อกัน
    return binary
# ฟังก์ชั่นที่ใช้ Stack ในการแปลงเลขฐาน 10 เป็นฐาน 16
def decimal_to_hexadecimal(n):
    stack = []  # สร้าง Stack
    hex_digits = "0123456789ABCDEF"  # ตัวเลขและตัวอักษรในฐาน 16
    # หากเลข n เป็น 0, ก็คืนค่าผลลัพธ์เป็น "0"
    if n == 0:
        return "0"
    while n > 0:
        stack.append(hex_digits[n % 16])  # เก็บเศษจากการหาร 16
        n = n // 16  # หาร n ด้วย 16
    hexadecimal = ""
    while stack:
        hexadecimal += stack.pop()  # นำตัวเลขใน Stack มาต่อกัน
    return hexadecimal
number = int(input("กรุณากรอกเลขฐาน 10: "))
# แปลงเลขจากฐาน 10 เป็นฐาน 2
binary_result = decimal_to_binary(number)
# แปลงเลขจากฐาน 10 เป็นฐาน 16
hexadecimal_result = decimal_to_hexadecimal(number)
print(f"เลขฐาน 2 ของ {number} คือ: {binary_result}")
print(f"เลขฐาน 16 ของ {number} คือ: {hexadecimal_result}")
