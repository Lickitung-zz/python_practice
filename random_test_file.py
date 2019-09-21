# Alright, this one can be tricky but I'm sure you can do it.

# Create a function named combo that takes two ordered iterables. 
# These could be tuples, lists, strings, whatever.

# Your function should return a list of tuples. 
# Each tuple should hold the first item in each iterable, 
# then the second set, then the third, and so on. 
# Assume the iterables will be the same length.

# Check the code below for an example.


# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(iter1, iter2):
    output = []
    for i in range(0, len(iter1)):
        output += (iter1[i], iter2[i]),
    return output

print(combo([1, 2, 3], 'abc'))