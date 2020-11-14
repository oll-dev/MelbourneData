# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

# Read in the dataset
dataset = pd.read_csv(r'Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnPrice = []

for p in dataset.Price:
    if math.isnan(p):
        pass
    else:
    #    plt.hist(p, color = 'blue', edgecolor = 'black')
        nnPrice.append(int(p))


plt.hist(nnPrice, color = 'blue', edgecolor = 'black')
plt.ylabel("Price")
plt.title("House prices")
plt.show()
