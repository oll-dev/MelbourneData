# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

# Read in the dataset
dataset = pd.read_csv(r'Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnRooms = []

for p in dataset.Rooms:
    if math.isnan(p):
        pass
    else:
    #    plt.hist(p, color = 'blue', edgecolor = 'black')
        nnRooms.append(int(p))

# print(nnPrice[1:40])
plt.hist(nnRooms, color = 'blue', edgecolor='black', bins='auto')
plt.axis([1, 9, 0, 16000])
plt.ylabel("Amount of houses")
plt.xlabel("Number of rooms")
plt.title("Rooms")
plt.show()
