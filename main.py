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
  
