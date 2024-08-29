'''Q. Create a program that takes a month (in number form) as input and prints the number of days in that month, considering leap years for February.'''

year = int(input("Enter the year: "))
month = int(input("Enter the month number (1-12): "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month in [4, 6, 9, 11]:
    days = 30
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 29  
    else:
        days = 28  
else:
    days = None  

if days:
    print(f"The number of days in month {month} of year {year} is {days}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")

'''Output
->Enter the year: 2024
->Enter the month number (1-12): 2
->The number of days in month 2 of year 2024 is 29.'''