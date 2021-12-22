# Julio Claros
# 114153234
# 2018-22-10
# Exercise

"""
Been looking at the exercises and this makes no sense to me...
"""

%matplotlib notebook
import matplotlib as plt
import pathlib
import path

namedir = path("names")
all_names = set()
years = list()
for path in namedir.glob('yob*.txt'):
    year = int(path.stem.split('yob')[1])
    years.append(year)
    #get all the name,sex,pairs in the file
    with path.open("r", encoding='utf-u8') as file:
        #union
        all_names |={l.rsplit(',', maxsplit=1)[0] for l in f if l.strip()}
years.sort()
print(len(all_names))

#build a dictionary whose keys are names, sex, pairs, and whose values are
#sequences of integers with one interger per year in the data. Add all zeros when a
#name is not listed for a given year

names = {name: list() for name in all_names}
paths = sorted(namedir.glob('yob*.txt'), key =lambda x: x.name)
    for p in paths:
        with p.open('r', encoding='utf-8') as f:
            nd = {
                k: int(v) for k, v in
                [l.rsplit(',', maxsplit=l) for l in f if l.strip()]

            }
            for name in names
                names[name].append(nd.get(name, 0))
    fig = plt.figure()
    ax = plt.axes()
    for name in ('Jack,M', 'Susie,F', 'John,M', 'Susan,F'):
        ax.plot(years, names[name], label=name)
        axe.set_title("basic names")
        axe.set_xlabel()