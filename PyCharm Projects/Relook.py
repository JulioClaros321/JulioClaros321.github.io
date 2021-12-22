# Julio Claros
# 114153234
# 2018-31-10
# Exercise
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('seaborn-whitegrid')

# Julio Claros
# 114153234
# 2018-25-10
# Exercise


import pandas as pd
import numpy as np
from lxml import etree
import matplotlib.pyplot as plt

school_name = dict()
df = pd.read_csv("PARCC_2017.csv")
x = df["School Name"]
for keys in x:
    kw = keys.lower()
    school_name[keys] = school_name.get(keys, 0) + 1
kws = sorted(school_name, key=school_name.get, reverse=True)
x = list(range(20))
y = [school_name[kw] for kw in kws[:20]]
fig = plt.figure()
ax = plt.axes()
plt.xlabel("schools)")
plt.plot(x, y)
plt.xticks(x, kws[:20], rotation="vertical")
plt.title("Hello")
plt.show()

def plot_data(text_file):

    Function passes a csv file and iterates through the lines to count the
    instances of crimes in certain neighborhoods in Seattle for the year 2018.
    Creates a line graph based on frequency of crimes in certain areas.

    Arg 1: text_file (Path to csv file): Csv file used as our data file for
    panda to load into a data frame

    Returns:
        A line graph based on the frequencies of crimes occurred during 2018
        in Seattle


    df = pd.read_csv(text_file)
    crimes = dict()
    x = df["Neighborhood"]
    for keys in x:
        crimes[keys] = crimes.get(keys, 0) + 1
    frequency = sorted(crimes.items())
    print(frequency)
    x, y = zip(*frequency)

    fig = plt.figure()
    ax = plt.axes()
    plt.plot(x, y)
    ax.set_xlabel("Seattle Neighborhoods")
    ax.set_ylabel("Number/Frequency of Crimes Occurred")
    ax.set_title("Crimes that Occurred in Seattle Neighborhoods (2018 Data)")
    plt.show()


if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    plt.style.use('seaborn-whitegrid')
    import numpy as np
    import sys
"""
