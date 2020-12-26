# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

# Read in the dataset
dataset = pd.read_csv(r'../Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnLand = []

# Disregard null values
for p in dataset.Landsize:
    if math.isnan(p):
        pass
    else:
        nnLand.append(int(p))

# Create plot
plt.hist(nnLand, color = 'blue', edgecolor='black', bins='auto')
plt.xlim(left=40, right=2000)
plt.ylabel("Number of houses")
plt.xlabel("Land size (m³)")
plt.title("Land size of houses")
plt.show()
