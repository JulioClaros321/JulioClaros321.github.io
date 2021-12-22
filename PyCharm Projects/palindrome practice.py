# Julio Claros
# 114153234
# 2018-1-10
# Assignment: Exercise Sets


def palindrome_checker(string):
    reverse = string[::-1]
    if string.casefold() == reverse.casefold(): return True
    else: return False


def extract_palindrome(input, output):
    with open(input, 'r') as inner:
        with open(output, 'w') as outter:
            for lines in inner:
                word = ''
                sentence = lines.strip()
                if not sentence:
                    continue
                else:
                    for chara in sentence:
                        if chara.isalnum():
                            word += chara
                        else:
                            continue
                if palindrome_checker(word):
                    outter.write(sentence + '\n')


if __name__ == '__main__':
    import sys
    extract_palindrome(sys.argv[1], sys.argv[2])
