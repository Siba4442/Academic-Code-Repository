''''Q. Write a program that takes three integers as input and determines 
    the largest among them using nested if statements ?'''

print("Enter three numbers to find the largest among them")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

print("The largest number is:", largest)

'''Output
->Enter three numbers to find the largest among them
->Enter the first number: 34
->Enter the second number: 56
->Enter the third number: 78
->The largest number is: 78'''