# Julio Claros
# 114153234
# 2018-1-1


def read_allowable(string):
    words = set()
    with open(string, "r") as file:
        for lines in file:
            sentence = lines.strip()
            if not sentence:
                continue
            else:
                words.add(sentence)
    return words
# start by throwing out the words that aren't allowed"
# loops over players, loop over words, loop over other players + their words
# Another approach, define an empty dict(): counts, loops over players, loop over unique words and count words by player. so if you find cat then its count goes up one and then u get list of how often a word appears,
# loop over players keep words only with the count of 1


def valid_words(dict, words):
    new_dic = {}
    dictionary = dict
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
        print(difference)
        for values in difference:
            if len(values) < 3 or values in allowable:
                continue
            else:
                allowable.add(values)
        new_dic[person] = allowable
    print(new_dic)


if __name__ == '__main__':
    import sys
    a = {"ron": ["dog", "I", "frog", "cat"], "Sue": ["dog", "fog", "he", "house"
    ],"Jamie": ["monkey,", "fox", "hehe"], "David": ["Trann", "donkey", "lol",
    "hehe",]}
    b = read_allowable(sys.argv[1])
    valid_words(a, b)


