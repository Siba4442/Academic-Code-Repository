#Write a python program to calculate the factorial of a numner N using loop

N = int(input("Enter a number N to find its factorial : "))
total_fac = 1  
if N >= 0: 
    for i in range(1, N+1) :
        total_fac *= i

print(f"The factorial {N} is {total_fac}")

'''Output
->Enter a number N to find its factorial : 0
->The factorial 0 is 1'''