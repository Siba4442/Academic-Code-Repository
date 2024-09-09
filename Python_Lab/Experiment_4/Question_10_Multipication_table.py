#Write  a python program to show the multipication table of an integer N using loop

num=int(input("Enter an integer to print its multipication table : "))
if num > 0:
    print(f"Multipication Table of {num}")
    for i in range(10):
        print(f"{num} X {i+1} = {num*(i+1)}")
else:
    print("invalid input , enter a positive number")

'''Output
->Enter an integer to print its multipication table : 12
->Multipication Table of 12
->12 X 1 = 12
->12 X 2 = 24
->12 X 3 = 36
->12 X 4 = 48
->12 X 5 = 60
->12 X 6 = 72
->12 X 7 = 84
->12 X 8 = 96
->12 X 9 = 108
->12 X 10 = 120'''