num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
sign = input("Enter a sign ( +, -, *, /):")

if sign == '+':
    result = num1 + num2
    print("Result:", result)
elif sign == '-':
    result = num1 - num2
    print("Result:", result)
elif sign == '*':
    result = num1 * num2
    print("Result:", result)
elif sign == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error!: Division by zero is not allowed")
else:
   print("Invalid operator!")
