'''4. Write a program that checks if a given year is a leap year. 
   A year is a leap year if it is divisible by 4, 
   but not divisible by 100, except if it is also divisible by 400.'''

year = int(input("Enter a year to find if it's a leap year or not: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

'''Output
->Enter a year to find if it's a leap year or not: 2024
->2024 is a Leap Year'''