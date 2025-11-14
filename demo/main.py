
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Không thể chia cho 0"
    return a / b

print("Kết quả cộng:", add(5, 3))
print("Kết quả trừ:", sub(10, 2))
print("Kết quả nhân:", mul(4, 5))
print("Kết quả chia:", div(20, 4))
