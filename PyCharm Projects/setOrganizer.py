# Julio Claros
# 114153234
# 2018-1-10
# Assignment: Exercises

names = ['Becky', 'Cinderella', 'Linda', 'Bobby', 'Christopher', 'Rayman', 'Drake', 'Antonio', 'Christian', 'Andrew']
names.sort(key=lambda s: len(s))
print(names)

numbs = [1, 2, 3, -1, -4, 20, 13, -8, -3, 6, 10, 7]
numbs.sort(key=lambda s: abs(s))
print(numbs)

order = [('Becky', 10), ('Chris', 5), ('Rayman', 600), ('Christian', 23)]
order.sort(key=lambda s: s[-1], reverse=True)
print(order)