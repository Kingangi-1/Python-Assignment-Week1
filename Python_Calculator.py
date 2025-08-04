#simple calculator program 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
  result = num1 + num2  
  print(result)

elif operation == '-'
result = num1 - num2
print(result)

elif operation == '*'
result = num1 * num2
print(result)

elif operation == '/'
if num2 != 0
print("Error! Division by zero."")
result = num1 / num2
print(result)
        else
print("Please enter a valid operator.")