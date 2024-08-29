'''12. Write a program that takes the lengths of three sides of a triangle as input and determines 
   whether the triangle is equilateral, isosceles, or scalene.'''

print("Enter only Intrger ->")

side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))

if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalenint")
    
'''Output
->Enter only Intrger ->
->Enter the length of the first side: 45
->Enter the length of the second side: 45
->Enter the length of the third side: 67
->The triangle is isosceles.'''