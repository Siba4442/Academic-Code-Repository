#Write a python program to check if the given string is palindrome or not using loop

str=input("Enter a string to check if its a Palindrome or not : ")
temp = ''
count = 0 
for i in str:
    count+=1
for i in range(count):
    temp = temp + str[count-1-i]

if temp == str:
    print("The entered is a palindrome")
else:
    print("The entered is not a palindrome")
    
'''Output
->Enter a string to check if its a Palindrome or not : mam 
->The entered is a palindrome'''