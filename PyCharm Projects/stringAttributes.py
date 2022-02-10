# Julio Claros
# 114153234
# 2018-10-09
# Assignment: Exercise P4E 6

"""Def hi_checker(Parameter of a string)
Stores string parameter in variable word and uses the string.find function to locate the string hi and stores an integer
value in hi_checker variable. Hi_checker returns either -1, meaning hi isnt in the word, or 0 - any whole number, meaning
that hi can be located within the word

if statements:

Arg: if hi_checker returns -1, print that your string doesn't contain hi
Arg 2: else print that your word does contain the substring hi
"""


def hi_checker(string):
    word = string
    checker = word.find('hi')

    if checker == -1:
        print("You word doesn't contain the substring hi")
    else:
        print("Your word does contain the substring hi")


"""def get_string(parameter of a string):
Stores string into variable word, which can used as an array later, and establishes variables first and last char as 
empty strings.

Print: (Prompt): length of word

if conditionals:

Arg 1: if (length of word) is equal to 0. Keep first and last char variables the same. Then print first and last char.

Arg 2: if (length of word) is equal to 1. First and last char variables changed to the value at word[0]. So they should 
take the value of the only letter in the string. Then print first and last char.

Arg 3: if (length of word) is greater than 1. First char set to word[0] and last char set to word[length of word - 1] 
because arrays start at 0. This should established their values as the first and last letters of the string. Then print
their values.

Call hi_checker function, print (prompt) and return of hi_checker function

If conditionals for printing out the center portion of variable word

Arg 1: if (length of word) < 3: 
Print: "sorry your word is to small"

Arg 2: else use the word.strip function to remove first_char and last_char from word variable and put the final string 
in middle_word. 
Print: (prompt) and value of middle_word

Print: (prompt) and return value of word.split() function, which separates every word individually
Print: (prompt) and return value of word.replace("is", "was"), which replaces all "is" strings with was

"""


def get_string(string):
    word = string
    first_char = ''
    last_char = ''

    print("The total length of your word is:", len(word))
    if len(word) == 0:
        first_char = ''
        last_char = ''
        print("The first character of your word is", first_char, "and the last character of your word is", last_char)
    elif len(word) == 1:
        first_char = word[0]
        last_char = word[0]
        print("The first character of your word is", first_char, "and the last character of your word is", last_char)
    else:
        first_char = word[0]
        last_char = word[len(word)-1]
        print("The first character of your word is", first_char, "and the last character of your word is", last_char)

    hi_checker(word)

    if len(word) < 3:
        print("Sorry your word is to small to print out just the middle portion")
    else:
        middle_word = word.strip(first_char)
        middle_word = middle_word.strip(last_char)
        print("Your word without the first and last characters is:", middle_word)

    print("You used the following words:", word.split())
    print("Changing every [is] with [was].....:", word.replace("is", "was"))


if __name__ == '__main__':
    get_string(input())