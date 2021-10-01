# Exercise 15: Reverse word order
# Ask the user for a long string, then print it out backwards to them
# Example: turn the string 'My name is Michele' into 'Michele is name My'
# Use a function - hint: split


def reverse_string():
    init_string = input('Tell me a story: ')
    final_string = init_string.split()
    final_string = final_string[::-1]
    final_string = ' '.join(final_string)
    return print(final_string)


reverse_string()

# Lessons: the steps for reversing order - name the list with BRACKETS
# list[::-1] will reverse the order of the list
# Once again, I created more variables than I needed while making the program and then went back around
# to clean up the program with only two variables. This is proof that it is possible with only one variable.
# Last note: setting up functions - no help_text needed at def line. Just put the text I want in input.
