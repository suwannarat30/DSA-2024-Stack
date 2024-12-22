def precedence(op):
    """ ฟังก์ชันสำหรับเปรียบเทียบลำดับความสำคัญของตัวดำเนินการ """
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def apply_operator(operand1, operand2, operator):
    """ ฟังก์ชันในการคำนวณค่าจากตัวดำเนินการ """
    if operator == '+':
        return operand1 + operand2
    if operator == '-':
        return operand1 - operand2
    if operator == '*':
        return operand1 * operand2
    if operator == '/':
        return operand1 / operand2

def infix_to_postfix(expression):
    """ ฟังก์ชันสำหรับแปลงนิพจน์จาก Infix เป็น Postfix """
    stack = []
    postfix = []
    number = ""  # ตัวแปรเพื่อเก็บตัวเลขหลายหลัก

    for char in expression:
        if char.isdigit():  # ถ้าเป็นตัวเลขให้เก็บไว้ในตัวแปร number
            number += char
        else:
            if number:
                postfix.append(number)  # เมื่อเจออักขระที่ไม่ใช่ตัวเลข ให้เพิ่มตัวเลขใน postfix
                number = ""  # รีเซ็ตตัวแปร number

            if char == '(':  # ถ้าเป็นวงเล็บเปิดให้เพิ่มไปใน Stack
                stack.append(char)
            elif char == ')':  # ถ้าเป็นวงเล็บปิดให้ Pop ตัวดำเนินการจาก Stack
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  # เอาวงเล็บเปิดออก
            else:  # ถ้าเป็นตัวดำเนินการ
                while (stack and precedence(stack[-1]) >= precedence(char)):
                    postfix.append(stack.pop())
                stack.append(char)

    # ถ้ามีตัวเลขที่ยังไม่ถูกเพิ่มใน Postfix
    if number:
        postfix.append(number)

    # หลังจากจบการอ่านแล้ว Pop ตัวดำเนินการที่เหลือออกจาก Stack
    while stack:
        postfix.append(stack.pop())

    return ' '.join(postfix)  # คั่นด้วยช่องว่างระหว่างตัวเลขและตัวดำเนินการ

def evaluate_postfix(postfix):
    """ ฟังก์ชันในการคำนวณค่าจาก Postfix Expression """
    stack = []
    tokens = postfix.split()  # แยกคำ (ตัวเลขหรือเครื่องหมาย) ด้วยช่องว่าง

    for token in tokens:
        if token.isdigit():  # ถ้าเป็นตัวเลข
            stack.append(int(token))
        else:  # ถ้าเป็นตัวดำเนินการ
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(operand1, operand2, token)
            stack.append(result)

    return stack.pop()

def evaluate_infix(expression):
    """ ฟังก์ชันในการประเมินผลนิพจน์ Infix """
    postfix = infix_to_postfix(expression)
    result = evaluate_postfix(postfix)
    return result

# รับค่าจากผู้ใช้งาน
expression = input("ป้อนนิพจน์ Infix (เช่น 3+(2*2)): ")

# ประเมินผล
result = evaluate_infix(expression)

# แสดงผลลัพธ์
print(f"ผลลัพธ์ของนิพจน์ {expression} คือ: {result}")
