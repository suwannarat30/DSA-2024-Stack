def reverse_string_using_stack(text):
    stack = []  # สร้าง Stack (ใช้ list)
    
    for char in text:
        stack.append(char)
    
    reversed_text = ""  # สตริงใหม่ที่จะเก็บข้อความที่กลับลำดับแล้ว
    
    # นำตัวอักษรจาก Stack ออกมาและสร้างข้อความที่กลับลำดับแล้ว
    while stack:
        reversed_text += stack.pop()
    
    return reversed_text
user_input = input("กรุณากรอกข้อความ: ")
result = reverse_string_using_stack(user_input)
print("ข้อความที่กลับลำดับแล้วคือ:", result)
