# Julio Claros
# 114153234
# 2018-25-10
# Exercise


def make_list(name):
    dictionary = dict()
    tree = etree.parse(name)
    for keyword in tree.xpath('//Keyword/text()'):
        kw = keyword.lower()
        dictionary[kw] = dictionary.get(kw, 0) + 1
    print(dictionary)


if __name__ == '__main__':
    import sys
    from lxml import etree
    make_list(sys.argv[1])
