# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

# Read in the dataset
dataset = pd.read_csv(r'../Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnPrice = []

# Disregard null values
for p in dataset.Price:
    if math.isnan(p):
        pass
    else:
        nnPrice.append(int(p))

# Create plot
plt.hist(nnPrice, color = 'blue', edgecolor='black', bins=1000)
plt.xlim(left=0, right=4000000)
plt.ylabel("Number of houses")
plt.xlabel("Price")
plt.title("House prices")
plt.show()
