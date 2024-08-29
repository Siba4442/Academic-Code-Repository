'''Q. Simulate a traffic light using conditionals. The user enters a color (red, yellow, or green), 
   and the program prints whether they should "Stop", "Ready", or "Go".'''

color = input("Enter the traffic light color (red, yellow, or green): ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color. Please enter red, yellow, or green.")

'''Output
->Enter the traffic light color (red, yellow, or green): Red 
->Stop'''