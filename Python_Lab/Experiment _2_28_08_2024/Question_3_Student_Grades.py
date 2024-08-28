'''Q. Create a program that takes a student's marks as input and prints their grade based on the following criteria:
   a. 90-100: A
   b. 80-89: B
   c. 70-79: C
   d. 60-69: D
   e. Below 60: F'''

total_marks = int(input("Enter the Total Marks of the Student out of 600: "))

if 0 <= total_marks <= 600: 
    percentage = (total_marks / 600) * 100
    print("The Percentage of the Student is", percentage)
    if 90 <= percentage <= 100:
        print("The Student's grade is A")
    elif 80 <= percentage < 90:
        print("The Student's grade is B")
    elif 70 <= percentage < 80:
        print("The Student's grade is C")
    elif 60 <= percentage < 70:
        print("The Student's grade is D")
    else:
        print("The Student's grade is F")
else:
    print("Invalid input, the input should be an integer in the range of 0 to 600")

'''Output
->Enter the Total Marks of the Student out of 600: 530
->The Percentage of the Student is 88.33333333333333
->The Student's grade is B'''