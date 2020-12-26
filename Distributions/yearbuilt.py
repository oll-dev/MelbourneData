# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

# Read in the dataset
dataset = pd.read_csv(r'../Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnYear = []

# Disregard null values
for p in dataset.YearBuilt:
    if math.isnan(p):
        pass
    else:
        nnYear.append(int(p))

# Create plot
plt.hist(nnYear, color = 'blue', edgecolor='black', bins='auto')
plt.xlim(left=1800, right=2030)
plt.ylabel("Number of houses")
plt.xlabel("Year built")
plt.title("Construction years")
plt.show()
