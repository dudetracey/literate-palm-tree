# Exercise 10: I am doing the same task as in Exercise 5 but in a new way.
# Rule: Use list comprehension
# Goal: given two lists, write a program that returns a list of the numbers that
# are included in both lists
import random
a = random.sample(range(100), 5)
print('Here is the first list: ')
print(a)
b = random.sample(range(105), 8)
print('Here is the second list: ')
print(b)
c = []
c = [x for x in a for y in b if x==y]
# At this point, the list will include duplicates.
# The set function fixes this by turning the list into a set
if len(c) == 0:
    print('There were no common values.')
else:
    print(set(c))
