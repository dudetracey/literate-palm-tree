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
