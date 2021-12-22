name_list = ['Annie', 'Trey', 'Bella', 'Kaitlin', 'Julio', 'Antonio', 'Rebecca', 'Relda']
name_list.sort(key=lambda n: len(n))
print(name_list)


integer_list = [-1, 2, 3, 4, 5, 6, 7, -8, -9, -20, -5]
integer_list.sort(key=lambda n: abs(n))
print(integer_list)

