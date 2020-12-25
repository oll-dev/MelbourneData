# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

# Read in the dataset
dataset = pd.read_csv(r'Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnBath = []

for p in dataset.Bathroom:
    if math.isnan(p):
        pass
    else:
    #    plt.hist(p, color = 'blue', edgecolor = 'black')
        nnBath.append(int(p))

# print(nnPrice[1:40])
plt.hist(nnBath, color = 'blue', edgecolor='black', bins='auto')
plt.xlim(left=0, right=6)
plt.ylabel("Number of houses")
plt.xlabel("Number of bathrooms")
plt.title("Bathrooms")
plt.show()
