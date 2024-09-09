#Write a python program to calculate X raised to the power Y using loop

print("Enter two integer X and Y to find X^Y : ")
X=int(input("Enter X : "))
Y=int(input("Enter Y : "))
temp_X = 1
for i in range(Y):
    temp_X*=X

print(f"{X}^{Y} = {temp_X}")

'''Output
->Enter two integer X and Y to find X^Y : 
->Enter X : 2
->Enter Y : 2
->2^2 = 4'''