# Exercise 4
# Goal: User gives a number, the program returns all divisors of that number.
a = int(input('Give me a number: '))
b = range(2, a+1)
c = []
for num in b:
    if a % num == 0:
        c.append(num)
print(c)
