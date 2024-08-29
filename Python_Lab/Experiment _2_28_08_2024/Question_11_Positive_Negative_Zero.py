'''Q. Create a program that categorizes a number as positive, negative, or zero.'''

print("Enter an integer -> ")

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

'''Output
->Enter a integer -> 
->Enter a number: -4
->The number is negative.'''