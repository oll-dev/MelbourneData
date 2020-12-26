# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

# Read in the dataset
dataset = pd.read_csv(r'../Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnDistance = []

# No null values
for p in dataset.Distance:
    nnDistance.append(float(p))

# Create plot
plt.hist(nnDistance, color = 'blue', edgecolor='black', bins='auto')
plt.ylabel("Number of houses")
plt.xlabel("Distance (km)")
plt.title("Distance from city center")
plt.show()
