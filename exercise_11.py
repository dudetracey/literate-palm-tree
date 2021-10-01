# Exercise 11: Checking if a number is prime.
# Goal: Ask the user for a number, then tell them if the number is prime.
# Hint: Use exercise 4 - divisors of a number

# Goal: User gives a number, the program returns all divisors of that number.
# We are using a function to get the number from the user.
def get_number(help_text='Give me a number: '):
    return int(input(help_text))


# This part looks just like exercise 4
a = get_number()
b = range(1, a + 1)
c = []
for num in b:
    if a % num == 0:
        c.append(num)

# Now c contains list of factors of the number given by the user. Two possible responses:

if len(c) == 2:
    print('Your number is prime. ')
else:
    print('The factors of your number include: ')
    print(c)
