def calculate(a, b):
    return a + b, a - b, a * b, a / b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

add, sub, mul, div = calculate(x, y)

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
