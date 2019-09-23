# Let's play with the *args pattern.

# Create a function named multiply that takes any number of arguments. 
# Return the product (multiplied value) of all of the supplied arguments. 
# The type of argument shouldn't matter.

# Slices might come in handy for this one.

def multiply(*args):
    sum = 0
    i = 0
    arg_len = len(*args)
    for arg in [*args]:
        print(arg[i])

numbers = [1, 2, 3, 4, 5, 6]
multiply(numbers)