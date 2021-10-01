# Exercise 2: Is the number odd or even?
# Version 1 of the odd and even
num = input('Give me a number: ')
num = int(num)
if num % 4 == 0:
    print('Your number is divisible by 4')
elif num % 2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')

#Version 2: Divisibility test
num = int(input('Give me a number you want to check: '))
check = int(input('Give me the number you want to try to divide by: '))
if num % check == 0:
    print('Yes, your number is divisible.')
else:
    print('No, your number is not divisible')
