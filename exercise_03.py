# Exercise 3 
# Write a program that prints out all the elements of a list that are less than 5.
# c variable is for checking the elements less than the user's input number.
def less_than_5():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    c = int(input('Give me a number to check: '))
    for num in a:
        if num < c:
            b.append(num)
    print(b)
return
