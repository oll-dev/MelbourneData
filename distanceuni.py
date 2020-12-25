# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

# Read in the dataset
dataset = pd.read_csv(r'Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnDistance = []

for p in dataset.Distance:
#    if math.isnan(p):
#        pass
#    else:
    #    plt.hist(p, color = 'blue', edgecolor = 'black')
    nnDistance.append(float(p))

# print(nnPrice[1:40])
plt.hist(nnDistance, color = 'blue', edgecolor='black', bins='auto')
# plt.xlim(left=0, right=6)
plt.ylabel("Number of houses")
plt.xlabel("Distance (km)")
plt.title("Distance from city center")
plt.show()
