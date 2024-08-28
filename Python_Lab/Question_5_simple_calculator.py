'''Q. Develop a simple calculator that takes two numbers and an operator (+,-,*,/) as input and prints the result. 
   Handle division by zero with an appropriate message.
'''

print("....Simple Calculator....")
print("Enter two Integer Value ->")

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the secound number : "))

print(f"Addition {num1} + {num2} = {num1 + num2}")
print(f"Substraction {num1} - {num2} = {num1 - num2}")
print(f"multipication = {num1} X {num2} = {num1 * num2}")
if num2 != 0:
    div = num1 / num2
else:
    print("Error: Division by zero is not allowed.")
