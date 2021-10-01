# Exercise 13
# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
# Try to do this in a function.
# Make sure the user is the one entering the number of numbers in the sequence to generate.

# Ideas: make the Fibonacci first, then make a function with the len() function


def get_number(help_text='Give me a number: '):
    return int(input(help_text))

# Here is the correct way to use the append function:
# lst = [1, 2, 3]
# lst.append(4)
# print(lst)
a = get_number()
fib = [1, 1]
previous_num = 1
current_num = 1
next_num = 0
while len(fib) < a:
    next_num = previous_num + current_num
    fib.append(next_num)
    previous_num = current_num
    current_num = next_num

print(fib)
