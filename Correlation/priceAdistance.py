# Import libraries
import pandas as pd
import math
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Read in the dataset
dataset = pd.read_csv(r'../Melbourne_housing_FULL.csv', skip_blank_lines=True)

# Initialize arrays
nnA = []
nnB = []

df = dataset[["Distance", "Price"]].dropna()
nnA = df.Distance
nnB = df.Price


# Calculate correlation
spearcorr = df.corr(method='spearman')
corrs, _ = np.corrcoef(nnA, nnB)
print("Pearsons: {}" .format(corrs))
print("Spearman: {}" .format(spearcorr))
plt.scatter(nnA, nnB)
plt.plot(np.unique(nnA), np.poly1d(np.polyfit(nnA, nnB, 1))(np.unique(nnA)), color='blue')
plt.show()
