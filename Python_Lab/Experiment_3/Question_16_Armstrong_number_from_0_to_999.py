#An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. 
#Write a program to find all Armstrong numbers in the range of 0 and 999.

print("All the Armstrong numbers in the range of 0 and 999")
for i in range(1000):
    sum = 0 
    digits = [int(d) for d in str(i)]
    for a in digits:
        sum += int(a)**3
    if sum == i:
        print(i)

'''Output
->All the Armstrong numbers in the range of 0 and 999
->0
->1
->153
->370
->371
->407'''