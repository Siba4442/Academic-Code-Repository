#Write a python program to count the number of digits in the integer N using loop

num=int(input("Enter a number  to find the number of digits in it : "))
count=0
if num > 0:
    while num > 0:
        num//=10
        count+=1
    print(f"The number of digits of the entered number is : {count}")
elif num == 0:
    count+=1
    print(f"The number of digits of the entered number is : {count}")
else:
    print("Invalid input, enter a positive integer") 

'''Output
->Enter a number  to find the number of digits in it : 123
->The number of digits of the entered number is : 3'''