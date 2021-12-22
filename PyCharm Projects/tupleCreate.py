# Julio Claros
# 114153234
# 2018-24-9
# Assignment: P4E 8
"""
Script that creates a list of tuples by opening a file of text
"""


def create_tuple(string):
    """
    Function that creates a list of tuples by taking in a string parameter that leads to a text file.
    Iterates through each line and of text file and singles out the string or proceeds to the next line
    if blank. Coverts string to tuple then adds it to the empty list variable.

    Arg:
        String (Path to text file): contains path to text file which is opened in reading mode

    Return:
        the_list[] (list of tuples): list of tuples compounded from text file in parameter.
    """
    the_list = []
    with open(string, "r") as file:
        for lines in file:
            sentence = lines.strip()
            if not sentence:
                continue
            else:
                tup = sentence.split("\t"),
                the_list.append(tup)
    print(the_list)
    return the_list


if __name__ == '__main__':
    import sys
    create_tuple(sys.argv[1])

