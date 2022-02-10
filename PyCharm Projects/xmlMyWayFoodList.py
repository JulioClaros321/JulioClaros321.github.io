# Julio Claros
# 114153234
# 2018-25-10
# Exercise

"""
Script that opens xml file of foods, and lists them
"""


def make_list(name):
    """
    Function passes an xml file and iterates through text and locates food names
    and adds them to empty list

    Arg 1: name (path to xml file) to iterate through tags to find food name
    elements

    Returns: food_list (list) list of name elements inside the food tags
    """
    file_name = name
    full_file = os.path.abspath(os.path.join(file_name))
    food_list = list()

    dom = ElementTree.parse(full_file)
    food = dom.findall("food/name")
    for f in food:
        food_list.append(f.text)
    return food_list


if __name__ == '__main__':
    import sys
    import os
    from xml.etree import ElementTree
    make_list(sys.argv[1])
