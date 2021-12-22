# Julio Claros
# 114153234
# 2018-1-1
# Assignment: Boggle Words HW
"""Script for a game of Boggle Words"""

import argparse
import sys


def open_file(readable):
    my_set = set()
    with open(readable, "r") as text_file:
        for lines in text_file:
            sentence = lines.strip()
            if not sentence: continue
            else:
                my_set.add(sentence)
    return my_set


def build_dict(adjective, adverbs, nouns, verbs):
    dictionary = {}
    dictionary["adj"] = adjective, dictionary["adv"] = adverbs,
    dictionary["n"] = nouns, dictionary["v"] = verbs
    return dictionary


def count_words(dictionary):
    for keys in dictionary:
        for values in keys:
            dictionary[keys] = dictionary.get(keys, 0) + 1


def read_allowable(string):
    """
    Function that passes a dictionary of usable words as a string, iterates
    through text file and places all words in a set

    Arg 1: string (String): List of usable words for Boggle Word game

    Returns:
        words (Set): A set of usable words for comparison.
    """
    words = set()
    with open(string, "r") as file:
        for lines in file:
            sentence = lines.strip()
            if not sentence:
                continue
            else:
                words.add(sentence)
    return words


def valid_words(guess, boggle):
    """
    Function that iterates through the values of a dictionary of player guesses
    to award points for unique words.

    Arg 1: guess (Dictionary): Individual players as keys and guesses as values
    Arg 2: boggle (text file): Text file of a dictionary of usable words

    Return:
        new_dic (Dictionary): Individual players as keys and unique guesses
        as values that obliged by the rules of Boggle Words
    """
    new_dic = {}
    dict[person] = list of values
    dictionary = guess
    for person in dictionary:
        player_guesses = set(dictionary[person])
        total = set()
        allowable = set()
        for people in dictionary:
            if people == person:
                continue
            else:
                guess = set(dictionary[people])
                total = total.union(guess)

        difference = player_guesses.difference(total)

        for values in difference:
            if len(values) < 3 or values in allowable or values not in boggle:
                continue
            else:
                allowable.add(values)
        new_dic[person] = allowable
    return new_dic


def get_words_from_user():
    """
    Allow the user to enter players' names and wordlists.

    Returns:
        (dict of str: list of str) A dictionary whose keys are player
        names and whose values are lists of the words found by each
        player.    
    """
    words = dict()
    while True:
        name = input('Enter the name of a player, or DONE to exit: ')
        name = name.strip()
        if name == 'DONE':
            break
        words[name] = list()
        while True:
            word = input('Enter a word found by {},\n'
                         'or DONE to finish entering words for this player: '
                         .format(name))
            word = word.strip()
            if word == 'DONE':
                break
            words[name].append(word)
    return words


def read_player_words(filename):
    """
    Read lists of words in filename.

    Args:
        filename (str): path to a text file containing words found in a
            game of Boggle. Lines in the file that end in a colon
            indicate the name of a player. Subsequent lines that do not
            end in a colon indicate the words found by that player.
            Below is an example of how the file should be formatted:

            Roger:
            cat
            cats
            clam
            calm

            Nicole:
            cat
            car
            carton
            cartoon

    Returns:
        (dict of str: list of str) A dictionary whose keys are player
        names and whose values are lists of the words found by each
        player.

    Raises:
        ValueError: a name occurs more than once in the file, or a word
        occurs before any names.
    """
    words = dict()
    name = None
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            if line[-1] == ':':
                name = line[:-1].strip()
                if name in words:
                    raise ValueError('error in word file {}: name "{}" occurs'
                                     ' more than once'.format(filename, name))
                else:
                    words[name] = list()
            elif name is None:
                raise ValueError('error in word file {}: word "{}" occurs'
                                 ' before the name of the player who found it'
                                 .format(filename, line))
            else:
                words[name].append(line)
    return words


def print_valid(valid):
    """
    Print the words found by each player that are worth points.

    Args:
        valid (dict of str: set of str): the words each player found
            that are worth points. Each key is a string containing a
            player's name; the corresponding value is a set of strings
            where each string is a word found by the player that is
            worth points.

    Side effects:
        prints output to stdout.
    """
    for name in sorted(valid):
        print('Words found by {} that are worth points:'.format(name))
        for word in sorted(valid[name]):
            print('    {}'.format(word))
        print()  # print a blank line at the end of each player's list


def parse_args(arglist):
    """
    Parse command-line arguments.

    Args:
        arglist (list of str): arguments from the command line.
            "--player_words" is an optional argument that should be
            followed by the name of a file containing words found by the
            players. The format of this file is described in
            read_player_words().

            allowable_words is a required argument; it should be the
            path to a file containing a wordlist. This list takes the
            place of a (paper) dictionary.

    Returns:
        (obj): an argument object as returned by
            argparse.ArgumentParser.parse_args().

    Side effects:
        If arglist contains the string "-h", a help statement will be
        printed to the console and the program will exit.
    """
    description = (
        "Given lists of words generated by Boggle players, identify the words"
        " that are worth points. Words are worth points if they are at least"
        " three letters long, appear in a standard English dictionary, and were"
        " found by only one player.\n"
        "\n"
        "This script can be used in two ways. The user can provide a path to a"
        " file where lines ending in a colon indicate a player's name and other"
        " lines indicate the words found by that player. Or, the script can be"
        " run with no command-line arguments, in which case it will prompt the"
        " user to enter the player's names and the words they found."
    )
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-p", "--player_words", help="optional file containing"
                        " words found by players. See description above for"
                        " information on the format of this file. If ommitted,"
                        " the user will be prompted to enter the words found"
                        " by players.")
    parser.add_argument("allowable_words", help="file containing all words for"
                        " which a player is allowed to earn points. Takes the"
                        " place of a dictionary.")
    args = parser.parse_args(arglist)
    return args


def boggle_words(arglist):
    args = parse_args(arglist)
    words = (get_words_from_user() if args.player_words is None
             else read_player_words(args.player_words))
    allowable = read_allowable(args.allowable_words)
    valid = valid_words(words, allowable)
    print_valid(valid)


if __name__ == '__main__':
    boggle_words(sys.argv[1:])
