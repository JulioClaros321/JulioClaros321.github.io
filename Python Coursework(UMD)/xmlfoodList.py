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
    food_list = list()
    tree = etree.parse(name)
    for keyword in tree.xpath('//food/name/text()'):
        food_list.append(keyword)
    print(food_list)


if __name__ == '__main__':
    import sys
    from lxml import etree
    make_list(sys.argv[1])
