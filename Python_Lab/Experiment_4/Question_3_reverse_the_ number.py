#Write a python programming to reverse a number using loop

num = int(input("Enter a number to find its reverse : "))

temp = num
result = 0
while temp > 0 : 
    rem = temp%10
    result = result*10+rem
    temp//=10

print(f"The reverse form of the number is {result}")

'''Output
->Enter a number to find its reverse : 123
->The reverse form of the number is 321'''