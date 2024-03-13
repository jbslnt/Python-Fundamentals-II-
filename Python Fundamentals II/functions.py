# functions
# - consists of function name, parameters
# - starts "def" keyword
# -  and make a block of code reusable.

# def averageOfThreeNumbers(num1, num2, num3):
#     #codes....
#     average = (num1 + num2 + num3) / 3
#     print("Average: ", average)


#SHORTCUT FOR COPYING HIGHLIGHTED/SINGLE LINE : alt + shift + ArrowDown/ArrowUp
# averageOfThreeNumbers(89, 76, 81)
# averageOfThreeNumbers(89, 76, 81)
# averageOfThreeNumbers(89, 76, 81)


# return function 
title = "Ang alamat ni loudie"
title2 = ": Bagsakan era"

def stringToTitle(title):
    return title.title()

def stringToUppercase(message):
    return message.upper()

def stringToLowercase(message):
    return message.lower()

def joinString(message, message2):
    return message.append(message2)

def countLetters(message):
    return len(message)

print(stringToTitle(title))
print(stringToUppercase(title))
print(stringToLowercase(title))
# print(joinString(title, title2))
print(countLetters(title))