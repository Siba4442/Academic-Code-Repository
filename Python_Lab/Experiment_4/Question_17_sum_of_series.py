#Compute the Sum Up to n Terms in the Series 1 - 1/2 + 1/3 - 1/4 + 1/5 -...+1/n

print("To find Sum up to n Terms in the Series 1 - 1/2 + 1/3 - 1/4 + 1/5 -...+1/n")
n = int(input("Enter the number of terms (n): "))
total_sum = 0.0
for i in range(1, n+1):
    if i % 2 == 0:
        total_sum -= 1 / i
    else:
        total_sum += 1 / i
print(f"The sum of the series up to {n} terms is: {total_sum}")

'''Output
->To find Sum up to n Terms in the Series 1 - 1/2 + 1/3 - 1/4 + 1/5 -...+1/n
->Enter the number of terms (n): 5
->The sum of the series up to 5 terms is: 0.7833333333333332'''