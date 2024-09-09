#Write a python program print the first N number of Fibonacci Number

num=int(input("Enter integer N to find the first N number of Fibonacci Numbers : "))
a, b = 0 , 1
for i in range(num): 
    print(a , end = ', ')
    a, b = b , a+b
print()

'''Output
->Enter integer N to find the first N number of Fibonacci Numbers : 12
->0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,'''