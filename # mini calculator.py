# mini calculator
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Cannot divide by zero!"
else:
    result = "Invalid operation"

print("Result:", result)
