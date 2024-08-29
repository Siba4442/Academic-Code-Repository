'''Q. Write a program that takes three integers as input and prints them in ascending order without using any built-in sorting functions.'''

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(f"The numbers in ascending order are: {a}, {b}, {c}")

'''Output
->Enter the first integer: 34
->Enter the second integer: 65
->Enter the third integer: 12
->The numbers in ascending order are: 12, 34, 65'''