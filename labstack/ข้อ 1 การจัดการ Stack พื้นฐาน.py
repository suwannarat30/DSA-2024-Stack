stack = []
# รับข้อมูลจากผู้ใช้เพื่อทำการ push
n = int(input("กรุณากรอกจำนวนข้อมูลที่ต้องการ push: "))
# ทดสอบการ push ข้อมูลตามจำนวนที่กรอก
for i in range(n):
    value = int(input(f"กรุณากรอกข้อมูลที่ {i+1}: "))
    stack.append(value)
# แสดงข้อมูลบนสุดโดยใช้ peek
if stack:  # ตรวจสอบว่า Stack ไม่ว่าง
    print("ข้อมูลบนสุดของ Stack (peek):", stack[-1])
else:
    print("Stack ว่าง!")
pop_count = min(3, len(stack))  # จำกัดการ pop ที่ 3 ตัว หรือจำนวนที่เหลือ
for _ in range(pop_count):
    popped_value = stack.pop()  # เอาค่าตัวบนสุดออก
    print(f"pop: {popped_value} ออกจาก Stack")
print("ข้อมูลที่เหลือใน Stack:", stack)
