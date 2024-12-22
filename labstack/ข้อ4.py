stack = []
json_string = input("กรุณากรอก JSON string: ")
i = 0  
is_valid = True  
while i < len(json_string):
    char = json_string[i]
    
    if char == '{' or char == '[':
        stack.append(char)  # เก็บเครื่องหมายเปิด
        
    elif char == '}' or char == ']':
        if not stack:
            is_valid = False  # ถ้า Stack ว่างแสดงว่าไม่มีเครื่องหมายเปิดตรงกัน
            break
        top = stack.pop()  # เอาเครื่องหมายเปิดออกจาก Stack
        if (char == '}' and top != '{') or (char == ']' and top != '['):
            is_valid = False  # ถ้าเครื่องหมายปิดไม่ตรงกับเครื่องหมายเปิด
            break
    elif char in [' ', '\n', '\t']:
        pass  
    elif char == '"':
        i += 1
        while i < len(json_string) and json_string[i] != '"':
            if json_string[i] == '\\':  # ตรวจสอบ escape sequence
                i += 1  
            i += 1
        if i >= len(json_string) or json_string[i] != '"':
            is_valid = False
            break
    else:
        pass  
    i += 1
if is_valid and len(stack) == 0:
    print("JSON string ถูกต้อง")
else:
    print("JSON string ไม่ถูกต้อง")
