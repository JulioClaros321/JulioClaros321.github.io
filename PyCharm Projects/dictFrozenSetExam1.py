# Julio Claros
# 114153234
# 2018-14-10
# Exam

"""
Function that iterates through list and counts instances of certain team face
offs.
"""


def count_matches(reading):
    """
    "Function takes text file parameter, and counts instances of team face offs
    by iterating though each lines. Distinction of readable line made by
    presence of character "v" in line.

    Args 1: reading (Path to text file) File opened in reading mode, then func.
    iterates through each line and count instances of teams facing off in a given
    year.

    Return:
        Dictionary (Dictionary). A dictionary that's keys consist of each
        team facing off. Values are the certain amount of instances that the
        same teams faced off regardless of order of the names. exp.
        Ohio State vs Penn State is another instance of Penn State v Ohio State
    """
    dictionary = {}
    the_list = list()
    with open(reading, "r") as text_file:
        for lines in text_file:
            sentence = lines.strip()
            if not sentence or sentence.find("v") < 0: continue
            else:
                tup = tuple(sentence.split(" v "))
                teams = frozenset(tup)
                the_list.append(teams)

        for keys in the_list:
            dictionary[keys] = dictionary.get(keys, 0) + 1

        return dictionary


if __name__ == '__main__':
    import sys
    count_matches(sys.argv[1])
