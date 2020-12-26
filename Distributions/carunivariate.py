# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

# Read in the dataset
dataset = pd.read_csv(r'../Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnCar = []

# Disregard null values
for p in dataset.Car:
    if math.isnan(p):
        pass
    else:
        nnCar.append(int(p))

# Create the plot
plt.hist(nnCar, color = 'blue', edgecolor='black', bins='auto')
plt.xlim(left=0, right=6)
plt.ylabel("Number of houses")
plt.xlabel("Car spots")
plt.title("Parking opportunity")
plt.show()
