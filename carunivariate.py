# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

# Read in the dataset
dataset = pd.read_csv(r'Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnCar = []

for p in dataset.Car:
    if math.isnan(p):
        pass
    else:
    #    plt.hist(p, color = 'blue', edgecolor = 'black')
        nnCar.append(int(p))

# print(nnPrice[1:40])
plt.hist(nnCar, color = 'blue', edgecolor='black', bins='auto')
plt.xlim(left=0, right=6)
plt.ylabel("Number of houses")
plt.xlabel("Car spots")
plt.title("Parking opportunity")
plt.show()
