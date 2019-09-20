# I need you to create a new function for me.

# This one will be named sillycase and it'll take a single string as an argument.

# sillycase should return the same string but the first half should be lowercased
# and the second half should be uppercased. 
# For example, with the string \"Treehouse\", sillycase would return \"treeHOUSE\".

# Don't worry about rounding your halves, but remember that indexes should be integers. 
# You'll want to use the int() function or integer division, //."



def sillycase(str):
    return str[:(len(str) // 2)].lower() + str[(len(str) // 2):(len(str))].upper()


print(sillycase("apple"))