#Write a python program to find sum of first Num
# number of natural number using a loop

Num = int(input("Enter a number Num to find the sum of Num natural number : "))
total_sum = 0
if Num > 0 :
    total_sum = Num*(Num+1/2)
    print("The sum of ", Num," natural number is : " , int(total_sum))
else: 
    print("Please entrer a valid input")
    
'''Output :
->Enter a number Num to find the sum of Num natural number : 10
->The sum of  10  natural number is :  105'''