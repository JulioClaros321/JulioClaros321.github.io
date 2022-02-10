# Julio Claros
# 114153234
# 2018-25-10
# Exercise

import matplotlib.pyplot as plt
from lxml import etree
import pandas as pd
import numpy as np
import matplotlib as mpl
plt.style.use('seaborn-whitegrid')

y = list()
tree = etree.parse("pubmed_result.xml")
counts = dict()
for keyword in tree.xpath("//Keyword/text()"):
    kw = keyword.lower()
    counts[kw] = counts.get(kw, 0) + 1
kws = sorted(counts, key=counts.get, reverse=True)

x = list(range(10))
y = [counts[kw] for kw in kws[:10]]
plt.xticks(x, kws[:10], rotation="vertical")

plt.plot(x, y, color="blue")
plt.show()
