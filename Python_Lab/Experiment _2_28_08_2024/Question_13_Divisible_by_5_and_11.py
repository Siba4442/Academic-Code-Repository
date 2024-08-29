#Q. Write a program that checks if a number is divisible by 5 and 11.

number = int(input("Enter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is not divisible by both 5 and 11.")

'''Output
->Enter a number: 24
->The number is not divisible by both 5 and 11.'''