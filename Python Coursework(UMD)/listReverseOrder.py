# Julio Claros
# 114153234
# 2018-1-10
# Assignment: Exercise Sets

text = 'Hai youngthug What gucci'
words = text.split()
t = list()
for word in words:
    t.append((len(word), word))
print(t)
t.sort(reverse=True)
print(t)
res = list()
for length, word in t:
    res.append(word)

print(res)


def count_tokens(tokens):
    count = []
    for token in tokens:
        token = token.casefold()
        count[token] = tokens.get(token, 0) +1