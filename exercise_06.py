# Exercise 6:
# Ask the user for a string, print out whether the string is a palindrome or not.
a = str(input('Give me a phrase: '))
b = a[::-1]
while len(a) > 2:
    if a.lower() == b.lower():
        print('Yes, this is a palindrome')
    else:
        print('No, this is not a palindrome')
    break
else:
    print('Please enter at least 2 characters.')

# So the key insight here was how to reverse the original string. The secret is to [::-1]
# I was actually really close but messed up the syntax. Make sure to do two : symbols
#The while loop was just a fun extension to make sure that a word long enough to be a palindrome was entered.
