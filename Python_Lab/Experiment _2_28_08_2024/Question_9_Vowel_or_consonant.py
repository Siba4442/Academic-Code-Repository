'''Q. Write a program that checks whether a given letter is a vowel or a consonant.'''

letter = input("Enter a letter: ").lower()

if letter in 'aeiou':
    print(f"{letter} is a vowel.")
elif letter.isalpha() and len(letter) == 1:
    print(f"{letter} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabetic character.")

'''Output
->Enter a letter: a
->a is a vowel'''