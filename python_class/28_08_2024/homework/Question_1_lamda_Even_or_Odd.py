'''Write a Program to check whether the number is even or odd Using Lamda'''

find = lambda x: "Even" if x % 2 == 0 else "Odd"
num = int(input("Enter a number: "))
result = find(num)
print(f"The number {num} is {result}.")

'''Output
->Enter a number: 5
->The number 5 is Odd.'''