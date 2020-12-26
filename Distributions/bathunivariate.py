# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

# Read in the dataset
dataset = pd.read_csv(r'../Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnBath = []

# Disregard null values
for p in dataset.Bathroom:
    if math.isnan(p):
        pass
    else:
        nnBath.append(int(p))

# Create the plot
plt.hist(nnBath, color = 'blue', edgecolor='black', bins='auto')
plt.xlim(left=0, right=6)
plt.ylabel("Number of houses")
plt.xlabel("Number of bathrooms")
plt.title("Bathrooms")
plt.show()
