# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

def word_count(string):
    dictionary = {}
    list_with_string = string.lower().split() # small chars in list
    for item in list_with_string:
        value = list_with_string.count(item)
        dictionary[item] = value
    return dictionary

print(word_count("I do not like it Sam I am"))