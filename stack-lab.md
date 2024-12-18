# การทดลองที่ 3: การใช้งานโครงสร้างข้อมูลแบบ Stack

## วัตถุประสงค์
1. เพื่อให้สามารถอธิบายหลักการทำงานของโครงสร้างข้อมูลแบบ Stack
2. เพื่อให้สามารถเขียนโปรแกรมจัดการ Stack ด้วยภาษา Python ได้
3. เพื่อให้สามารถประยุกต์ใช้ Stack ในการแก้ปัญหาได้

## อุปกรณ์ที่ใช้
1. เครื่องคอมพิวเตอร์
2. Python IDE (เช่น PyCharm, VS Code)
3. ใบงานการทดลอง

## ทฤษฎีที่เกี่ยวข้อง
Stack เป็นโครงสร้างข้อมูลแบบ LIFO (Last In First Out) คือ ข้อมูลที่เข้ามาทีหลังจะถูกนำออกก่อน เปรียบเสมือนการวางจานซ้อนกัน การจัดการข้อมูลใน Stack มีการดำเนินการพื้นฐาน เช่น :
1. Push: การเพิ่มข้อมูลเข้า Stack
2. Pop: การนำข้อมูลออกจาก Stack
3. is_empty: ตรวจสอบว่า Stack ว่างหรือไม่

## การทดลอง

### ส่วนที่ 1: การสร้าง Stack พื้นฐาน

```python
class Stack:
    def __init__(self):
        """สร้าง Stack เปล่า"""
        self.items = []     # ใช้ list เก็บข้อมูลใน Stack
    
    def is_empty(self):
        """ตรวจสอบว่า Stack ว่างหรือไม่"""
        return len(self.items) == 0
    
    def push(self, item):
        """เพิ่มข้อมูลเข้า Stack"""
        self.items.append(item)
    
    def pop(self):
        """นำข้อมูลออกจาก Stack"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        """ดูข้อมูลที่อยู่บนสุดของ Stack"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def size(self):
        """ดูขนาดของ Stack"""
        return len(self.items)
```

**คำอธิบายการทำงาน:**
- `__init__()`: สร้าง Stack เปล่าโดยใช้ list เก็บข้อมูล
- `is_empty()`: ตรวจสอบว่า Stack ว่างหรือไม่
- `push()`: เพิ่มข้อมูลที่ด้านบนของ Stack
- `pop()`: นำข้อมูลออกจากด้านบนของ Stack
- `peek()`: ดูข้อมูลที่อยู่ด้านบนโดยไม่นำออก
- `size()`: ดูจำนวนข้อมูลใน Stack

### ส่วนที่ 2: การทดสอบการทำงานพื้นฐาน

```python
def test_basic_operations():
    # สร้าง Stack ใหม่
    stack = Stack()
    
    # ทดสอบ push
    print("1. ทดสอบการ push ข้อมูล:")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack หลัง push: {stack.items}")
    
    # ทดสอบ peek
    print("\n2. ทดสอบการ peek:")
    print(f"ข้อมูลบนสุด: {stack.peek()}")
    
    # ทดสอบ pop
    print("\n3. ทดสอบการ pop:")
    print(f"ข้อมูลที่ pop: {stack.pop()}")
    print(f"Stack หลัง pop: {stack.items}")
    
    # ทดสอบ size
    print("\n4. ทดสอบการหาขนาด:")
    print(f"ขนาดของ Stack: {stack.size()}")
```

### ส่วนที่ 3: การประยุกต์ใช้ Stack 
#### 1. การตรวจสอบวงเล็บ

```python
def check_parentheses(expression):
    """ตรวจสอบความถูกต้องของวงเล็บในนิพจน์"""
    stack = Stack()
    
    # วนตรวจสอบแต่ละตัวอักษร
    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    
    # ถ้า Stack ว่าง แสดงว่าวงเล็บถูกต้อง
    return stack.is_empty()

# ทดสอบการใช้งาน
expressions = ['((()))', '((())', '(())', ')(']
for exp in expressions:
    result = check_parentheses(exp)
    print(f"นิพจน์ {exp} {'ถูกต้อง' if result else 'ไม่ถูกต้อง'}")
```

#### 2. การแปลงนิพจน์ Infix เป็น Postfix
```python
def infix_to_postfix(expression):
    """แปลงนิพจน์จากรูปแบบ Infix เป็น Postfix"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    postfix = []
    
    for char in expression:
        if char.isalnum():  # ถ้าเป็นตัวเลขหรือตัวอักษร
            postfix.append(char)
        elif char == '(':   # ถ้าเป็นวงเล็บเปิด
            stack.push(char)
        elif char == ')':   # ถ้าเป็นวงเล็บปิด
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()     # pop วงเล็บเปิดทิ้ง
        else:              # ถ้าเป็นตัวดำเนินการ
            while (not stack.is_empty() and stack.peek() != '(' and 
                   precedence.get(stack.peek(), 0) >= precedence.get(char, 0)):
                postfix.append(stack.pop())
            stack.push(char)
    
    # Pop ตัวดำเนินการที่เหลือ
    while not stack.is_empty():
        postfix.append(stack.pop())
    
    return ''.join(postfix)

# ตัวอย่างการใช้งาน
expr = "a+b*(c^d-e)^(f+g*h)-i"
print(f"Infix: {expr}")
print(f"Postfix: {infix_to_postfix(expr)}")
```

#### 3. การตรวจสอบ HTML Tags
```python
def check_html_tags(html):
    """ตรวจสอบความถูกต้องของ HTML tags"""
    stack = Stack()
    i = 0
    while i < len(html):
        if html[i] == '<':
            tag = ""
            i += 1
            while i < len(html) and html[i] != '>':
                tag += html[i]
                i += 1
            
            if tag.startswith('/'):  # Closing tag
                if stack.is_empty() or stack.pop() != tag[1:]:
                    return False
            else:  # Opening tag
                if not tag.startswith('!') and not tag.startswith('?'):
                    stack.push(tag)
        i += 1
    
    return stack.is_empty()

# ตัวอย่างการใช้งาน
html = "<html><body><p>Hello</p></body></html>"
print(f"HTML tags {'ถูกต้อง' if check_html_tags(html) else 'ไม่ถูกต้อง'}")
```

#### 4. การจำลองระบบ Call Stack
```python
class CallStack:
    def __init__(self):
        self.stack = Stack()
    
    def function_call(self, func_name, params=None):
        """จำลองการเรียกฟังก์ชัน"""
        frame = {
            'function': func_name,
            'parameters': params,
            'local_vars': {}
        }
        self.stack.push(frame)
        print(f"Calling {func_name}")
        self.display_stack()
    
    def return_from_function(self):
        """จำลองการ return จากฟังก์ชัน"""
        if not self.stack.is_empty():
            frame = self.stack.pop()
            print(f"Returning from {frame['function']}")
            self.display_stack()
    
    def display_stack(self):
        """แสดง call stack ปัจจุบัน"""
        print("\nCall Stack:")
        for frame in reversed(self.stack.items):
            print(f"- {frame['function']}({frame['parameters']})")
        print()

# ตัวอย่างการใช้งาน
call_stack = CallStack()
call_stack.function_call('main')
call_stack.function_call('factorial', 5)
call_stack.function_call('multiply', [5, 4])
call_stack.return_from_function()
call_stack.return_from_function()
```

## แบบฝึกหัดระหว่างการทดลอง
### แบบฝึกหัดที่ 1: การจัดการ Stack พื้นฐาน
1. สร้าง Stack และทดสอบการ push ข้อมูล 5 ตัว
2. แสดงข้อมูลบนสุดโดยใช้ peek
3. ทดสอบ pop ข้อมูลออก 3 ตัว
4. แสดงข้อมูลที่เหลือใน Stack

## แบบทดสอบท้ายการทดลอง
### 1.โปรแกรมกลับลำดับตัวอักษร
    จงเขียนโปรแกรมกลับลำดับตัวอักษรในข้อความโดยใช้ Stack (รับข้อความมาจากผู้ใช้งาน)

### 2.โปรแกรมแปลงเลขฐาน
    จงเขียนโปรแกรมแปลงเลขฐาน 10 ให้เป็นฐาน 2 และ ฐาน 16 โดยใช้ Stack และทดสอบเรียกใช้งานโดยรับตัวเลขฐาน 10 มาจากผู้ใช้งาน

#### 3: การคำนวณ Postfix Expression
    จงเขียนฟังก์ชันสำหรับคำนวณผลลัพธ์ของนิพจน์ในรูปแบบ Postfix และทดสอบเรียกใช้งานโดยให้ผู้ใช้ป้อน Postfix Expression

#### 4: การตรวจสอบ JSON string
    จงเขียนโปรแกรมตรวจสอบความถูกต้องของ JSON string โดยใช้ Stack และทดสอบเรียกใช้งานโดยให้ผู้ใช้งานป้อน JSON string

#### ส่วนที่ 5: คำนวณ Infix ด้วย Stack
   จงเขียนฟังก์ชันประเมินผลนิพจน์คณิตศาสตร์ที่อยู่ในรูป Infix โดยใช้ Stack และทดสอบการทำงานโดยป้อน infix Expression จากผู้ใช้งาน


## การส่งงาน
1. ส่งไฟล์ .py ที่มีโค้ดทั้งหมด
2. กำหนดส่ง: [วันที่ 24 ธันวาคม 2567]

