def evaluate_postfix(expression):
    stack = []  # สร้าง Stack เพื่อเก็บตัวเลข
    # แยกคำในนิพจน์ Postfix
    tokens = expression.split()
    # วนลูปแต่ละ token (ตัวเลขหรือโอเปอเรเตอร์)
    for token in tokens:
        if token.isdigit():  # ถ้า token เป็นตัวเลข
            stack.append(int(token))  # นำตัวเลขใส่ใน Stack
        else:  # ถ้า token เป็นโอเปอเรเตอร์
            b = stack.pop()  # นำตัวเลข 2 ตัวสุดท้ายจาก Stack
            a = stack.pop()
            
            if token == '+':  # การบวก
                stack.append(a + b)
            elif token == '-':  # การลบ
                stack.append(a - b)
            elif token == '*':  # การคูณ
                stack.append(a * b)
            elif token == '/':  # การหาร
                if b != 0:
                    stack.append(a / b)  # การหาร
                else:
                    return "Error: Division by zero"
    
    # ผลลัพธ์สุดท้ายจะอยู่ใน Stack
    return stack[0] if stack else "Error: Invalid Expression"
# รับค่าจากผู้ใช้
postfix_expression = input("กรุณากรอกนิพจน์ Postfix (ใช้ช่องว่างคั่นระหว่างตัวเลขและโอเปอเรเตอร์): ")
# เรียกใช้งานฟังก์ชั่นเพื่อคำนวณผลลัพธ์
result = evaluate_postfix(postfix_expression)
print(f"ผลลัพธ์ของนิพจน์ Postfix คือ: {result}")
