'''6. Write a program that takes the coordinates of a point (x, y) and determines which quadrant
   the point lies in (I, II, III, IV).'''
   
print("Enter two integer Value")

x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

print(f"The point ({x}, {y}) lies in :" , end = (' '))

if x > 0 and y > 0:
    print("I (First Quadrant)")
elif x < 0 and y > 0:
    print("II (Second Quadrant)")
elif x < 0 and y < 0:
    print("III (Third Quadrant)")
elif x > 0 and y < 0:
    print("IV (Fourth Quadrant)")
elif x == 0 and y == 0:
    print("the origin")
elif x == 0:
    print("on the Y-axis")
elif y == 0:
    print("on the X-axis")

''''Output
->Enter two integer Value
->Enter the x-coordinate: 34
->Enter the y-coordinate: 43
->The point (34, 43) lies in : I (First Quadrant)'''