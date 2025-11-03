print("Welcome to the Calculator")



# Ask user for first number

num1 = float(input("Enter the first number: "))



# Ask user for operation

operation = input("Choose an operation (+, -, *, /): ")



# Ask user for second number

num2 = float(input("Enter the second number: "))



# Perform calculation

if operation == "+":

    result = num1 + num2

elif operation == "-":

    result = num1 - num2

elif operation == "*":

    result = num1 * num2

elif operation == "/":

    if num2 != 0:

        result = num1 / num2

    else:

        result = "Error: Division by zero!"

else:

    result = "Invalid operation!"



# Show result

print("✅ Result:", result)