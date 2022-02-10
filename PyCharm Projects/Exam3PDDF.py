# Julio Claros
# 114153234
# 2018-13-11
# HW 6
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("exchange_rates.csv")
x = df["Date"]
y = df["Euro"]

plt.plot(x, y)
plt.show()
