# Question 5

import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('heart.csv')

data = dataset.iloc[:,:-1]
labels = dataset.iloc[:, -1] 

fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20,10))

data.plot(ax=ax.flatten()[:len(data.columns)], kind='box', subplots=True, sharex=False, sharey=False)

fig.tight_layout()
plt.show()
