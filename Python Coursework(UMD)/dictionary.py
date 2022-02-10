# Julio Claros
# 114153234
# 2018-1-10
# Assignment: P4E 9
"""
Script that takes a text file and converts it into a dictionary
"""


def make_dictionary(string):
    """
    Function that takes a parameter of a text file path, then it converts it into a list and add list contents
    to dictionary

    Arg 1: String (Path to text file): iterates through text file lines and adds them to list

    Returns:
           A dictionary of tuples
    """
    dictionary = dict()
    the_list = []
    with open(string, "r") as file:
        for line in file:
            sentence = line.strip()
            if not sentence:
                continue
            else:
                tup = sentence.split('\t')
                the_list.append(tup)
    dictionary = dict(the_list)
    return dictionary


if __name__ == '__main__':
    import sys
    make_dictionary(sys.argv[1])



