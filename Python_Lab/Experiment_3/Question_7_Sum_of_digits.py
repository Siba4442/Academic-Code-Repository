#Write a python program to find the sum of digits of a given integer N

num=int(input("Enter an integer N to find the sum of its digits : "))
total=0
if num >= 0:
    for i in range(num):
        rem = num%10
        total+=rem
        num//=10
else:
    print("Invalid input")
print(f"The sum of the digits of the given number is : {total}")  

'''Output
->Enter an integer N to find the sum of its digits : 123
->The sum of the digits of the given number is : 6'''