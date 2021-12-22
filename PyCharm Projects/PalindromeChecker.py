# Julio Claros
# 114153234
# 2018-24-9
# Assignment: Hw 3
"""
Script that checks for palindromes in one file and prints them in another
"""


def is_palindrome(string):
    """
    Function that takes a string parameter and compares it with the string spell
    -ed backwards. Validates if its a true palindrome.

    Arg 1: string (string): lines of text that it receives from function extract
    palindrome.

    Return: (True/False) (Boolean): dependant on if string is a true palindrome
        """
    word = ""
    for chara in string:
        if chara.isalnum():
            word += chara.casefold()
    reverse = word[::-1]
    if word.casefold() == reverse.casefold():
        return True
    else:
        return False


def extract_palindrome(reading, writing):
    """
    Extracts true palindromes from one text file using the empty string "Word"
    variable and prints them in another text file

    Arg 1: reading (Path to text file/Input file): File opened for reading,
    which then it iterates through each line and extracts true palindromes

    Arg 2: writing (Path to text file/Output file): File opened for writing,
    which then it prints out lines that are true palindromes conjured from input
    file.

    Return:
        No return value (N/A)
    """
    with open(reading, "r") as input_file, open(writing, "w") as output_file:
            for lines in input_file:
                sentence = lines.strip()
                if not sentence:
                    continue

                if is_palindrome(sentence):
                    output_file.write(sentence + "\n")


if __name__ == '__main__':
    import sys
    extract_palindrome(sys.argv[1], sys.argv[2])
