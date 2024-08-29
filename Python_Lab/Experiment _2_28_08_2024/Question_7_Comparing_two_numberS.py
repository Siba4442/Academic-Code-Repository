'''Q. Create a program that asks the user to input two numbers and then prints whether 
   the first number is greater than, less than, or equal to the second number.
'''
print("Enter two number to compare ->")

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the Secound number : "))

if num1 > num2:
    print(f"The First number {num1} is Greater then the secound number {num2}. ")
elif num1 == num2:
    print(f"The First number {num1} is Equal to secound number {num2}. ")
else:
    print(f"The First number {num1} is Less then the secound number {num2}. ")

'''Output
->Enter two number to compare ->
->Enter the first number : 54
->Enter the Secound number : 23
->The First number 54 is Greater then the secound number 23.'''