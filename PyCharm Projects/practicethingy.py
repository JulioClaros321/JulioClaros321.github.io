def encrypt(word):
    counter = 0
    word = [word.lower()]
    for letters in word:
        if letters == "a":
            word.replace(0)
        counter + 1
    return word

if __name__ == '__main__':
    print(encrypt("APPLES"))