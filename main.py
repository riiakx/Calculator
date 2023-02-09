print("Welcome to my Calculator")
print("1) Addition (+)")
print("2) Subtraction (-)")
print("3) Division (/)")
print("4) Multiplication (*)")

operation = input("Enter an operation: ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "/":
    print(num1 / num2)

