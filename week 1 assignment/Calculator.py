# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to choose a mathematical operation
print("Choose an operation: addition, subtraction, multiplication, or division")
operation = input("Enter the operation: ").strip().lower()

# Perform the operation based on the user's input
if operation == "addition":
    result = num1 + num2
    print("Result:", result)
elif operation == "subtraction":
    result = num1 - num2
    print("Result:", result)
elif operation == "multiplication":
    result = num1 * num2
    print("Result:", result)
elif operation == "division":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose addition, subtraction, multiplication, or division.")
gg