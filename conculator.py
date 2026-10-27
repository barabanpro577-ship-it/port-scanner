num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
op = input("Enter the operator:")
if op == "+":
    print("the addition is:", num1 + num2)
elif op == "-":
    print("the subtraction is:", num1 - num2)
elif op == "*":
    print("the multiplication is:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("the division is:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
        
