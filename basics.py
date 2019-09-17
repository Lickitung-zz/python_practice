# print(int("11"))
# print(float(11))
# number_of_burrito_characters = len("burrito")
# print(number_of_burrito_characters)

def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 2)
    print(result)

yell("I did a python thingy")