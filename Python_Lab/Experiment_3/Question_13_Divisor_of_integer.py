#Write a pyton program to print all the divisor an integer H using loop 

num=int(input("Enter an integer to find all its divisor : "))

if num > 0:
    print(f"The divisor of {num} are :")
    for i in range(1 , (num//2+1) ):
        if num % i == 0:
            print(i)
else:
    print("Invalid input, Enter an positive intrger")
    
'''Output
->Enter an integer to find all its divisor : 12
->The divisor of 12 are :
->1
->2
->3
->4
->6'''