# Exercise 5:
# Goal: given two lists, write a program that returns a list of the numbers that are included in both lists
def included():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    c = []
    for num in a:
        if num not in c:
            if num in b:
                c.append(num)
    print (c)
