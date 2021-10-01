# Exercise 10: I am doing the same task as in Exercise 5 but in a new way.
# Rule: Use list comprehension
# Goal: given two lists, write a program that returns a list of the numbers that
# are included in both lists

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
c = []
c = [x for x in a for y in b if x not in c and x==y]
# At this point, the list will include duplicates.
# The set function fixes this by turning the list into a set
print(set(c))
