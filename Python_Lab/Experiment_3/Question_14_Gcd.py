#Write a python program to find the Greatest Common Divisor (GCD) of two number using loop

print("Enter two numbers to find the greatest common divisor between them:")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

min_value = num1 if num1 < num2 else num2
gcd = 1 

for i in range(1, min_value + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print(f"The Greatest Common Divisor (GCD) of {num1} and {num2} is: {gcd}")

'''Output
->Enter two numbers to find the greatest common divisor between them:
->Enter the first number: 12
->Enter the second number: 6
->The Greatest Common Divisor (GCD) of 12 and 6 is: 6'''