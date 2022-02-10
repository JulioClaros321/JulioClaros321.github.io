# Julio Claros
# 114153234
# October 30, 2018
# Quiz

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("distance_and_drive_time.csv")
x = df["Distance"]
y = df["Drive_time"]

fig = plt.figure()
ax = plt.axes()

plt.xlabel("Distances (Miles)")
plt.ylabel("Drive Time (Minutes)")
plt.title("Distance and drive time to various locations from UMD")

plt.scatter(x, y, color="blue")
plt.show()

