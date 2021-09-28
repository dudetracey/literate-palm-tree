# Is it possible to combine all my practice exercises into one repo on Github? This would be proof that I have completed all the exercises.
# Maybe there is a way to make a menu to choose which exercise I want to show.
# The menu is probably best written as a function. Maybe I create all the different activities as functions and then I make a function that asks for which function.
# Yes, that means a function of functions.


# Create a function that gives the first and last entries in a list
import random


def first_last():
    return print(a[0], a[-1])


a = random.sample(range(1000), 7)
a = sorted(a)
print(a)
b = [first_last()]




# Write a program that prints out all the elements of a list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55 , 89]
for num in a:
  if a < 5:
    print(num)
  
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


# Exercise 14: List Remove Duplicates
# Write a function that takes a list and returns a new list that contains all the elements
# of the first list minus all the duplicates

# Extras:
# Write two different functions - one using a loop and constructing a list, and the other in sets
# Go back and do Exercise 5 using sets and write the solution for that in a different function


lst1 = [1, 1, 2, 3, 5, 6, 7, 8, 8, 9, 10, 10, 11, 11, 11, 11, 11, 13, 14]
lst2 = []


# Method 1: using a loop


def duplicates():
    for x in lst1:
        if x not in lst2:
            lst2.append(x)
    return print(lst2)


print('Original list', lst1)
print('Cleaned up list, no more duplicates:')
duplicates()

# Method 2: using sets
lst3 = ['Michelle', 'Adjovi', 'Michelle', 'Kendra', 'Adeyinka', 'Adeyinka', 'Naomi', 'Dekontee']


def set_dupes():
    return print(set(lst3))


print('Here is a list of names. ', lst3)
print('Here is the set form of that list. ')
set_dupes()

# Exercise 5 repeated in a function
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


def common(a, b):
    c = [x for x in a if x in b]
    return set(c)


print('Here is exercise 5 done again in a function: ')
print(common(a, b))

