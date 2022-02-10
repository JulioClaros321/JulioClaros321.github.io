# Julio Claros
# 114153234
# 2018-27-10
# Hw 5
"""
Script that takes a csv file (Crime_Data.csv) and counts occurrences of crimes
in Seattle for graphing.
"""


def plot_data(text_file):
    """
    Function passes a csv file and iterates through the lines to count the
    instances of crimes in certain neighborhoods in Seattle for the year 2018.
    Creates a line graph based on frequency of crimes in certain areas.

    Arg 1: text_file (Path to csv file): Csv file used as our data file for
    panda to load into a data frame

    Returns:
        A line graph based on the frequencies of crimes occurred during 2018
        in Seattle

    """
    df = pd.read_csv(text_file)
    crimes = dict()
    x = df["Neighborhood"]
    for keys in x:
        crimes[keys] = crimes.get(keys, 0) + 1
    kws = sorted(crimes, key=crimes.get, reverse=True)
    numb = len(kws)
    x = list(range(numb))
    y = [crimes[keys] for keys in kws[:numb]]
    fig = plt.figure()
    ax = plt.axes()
    plt.plot(x, y)
    plt.xticks(x, kws[:numb], rotation="vertical")
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
    plot_data(sys.argv[1])
