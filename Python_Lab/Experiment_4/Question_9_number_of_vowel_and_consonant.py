str = input("Enter a string to find the number of vowel and consonant in the string : ")
list1 = ['a' , 'e' , 'i' , 'o' , 'u']
count=0
con_count=0
for char in str:
    if char in list1:
        count+=1
    elif char.isalpha() and char != ' ':
        con_count+=1
print(f"The number of vowel in the entered string is : {count}")
print(f"The number of consonant in the entered string is : {count}")

'''Output
->Enter a string to find the number of vowel and consonant in the string : siba prasad sahu
->The number of vowel in the entered string is : 6
->The number of consonant in the entered string is : 6'''