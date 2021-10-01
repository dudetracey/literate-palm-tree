# Exercise 7:
# Given a list, make a new list that has only the even elements of the list. Try to do it in one line of code.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if x % 2 == 0]
print(b)

# Ok, so the key here is the correct formatting. x for x in list if ______
