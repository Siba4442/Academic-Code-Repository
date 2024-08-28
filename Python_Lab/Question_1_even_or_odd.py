''' Q. Write a program that asks the user
    to enter an integer and checks whether the number is even or odd ?'''

num = int(input("Enter a number to check weather its even or odd : "))
print("The entered number is Even" if num % 2 == 0 else "The entered number is Odd")

'''Output
->Enter a number to check weather its even or odd : 5
->The entered number is Odd'''