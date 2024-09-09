#Write a python program to find if a number is  prime or not using loop

num = int(input("Enter a number to find if its Prime or not : "))
N = num//2
for i in range(2 , N+1):
    if num % i == 0:
        print(f"The number {num} is not a prime number")
        break
    else:
        print(f"The number {num} is a prime number")

'''Output
->Enter a number to find if its Prime or not : 5  
->The number 5 is a prime number'''