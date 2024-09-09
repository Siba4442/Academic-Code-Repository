#Write a python program to find the largest number in the List using loop

num = int(input("Enter the length of the list: "))
list1 = []

for i in range(num):
    element = int(input(f"Enter element {i+1}: "))
    list1.append(element)

max_value = list1[0]

for i in range(1, num):
    if list1[i] > max_value:
        max_value = list1[i]

print(f"The largest number in the list is: {max_value}")

'''Output
->Enter the length of the list: 3
->Enter element 1: 12
->Enter element 2: 13
->Enter element 3: 34
->The largest number in the list is: 34'''