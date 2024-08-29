'''8. Write a program that takes a student's score as input and determines if they passed or failed. 
   The passing score is 50 or higher.'''

print("....Result....")

score = int(input("Enter the student's score: "))

result = "Passed" if score >= 50 else "Failed"
print(f"Student has {result} the exam.")

'''Output
->....Result....
->Enter the student's score: 45
->Student has Failed the exam.'''