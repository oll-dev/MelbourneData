# Import libraries
import pandas as pd
import math
import numpy
from scipy import stats

# Read in the dataset
dataset = pd.read_csv(r'../Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnArr = []

# Disregard null values
for p in dataset.Price:
    if math.isnan(p):
        pass
    else:
        nnArr.append(int(p))


# Calculate mean
mean = numpy.mean(nnArr)
# Calculate median
median = numpy.median(nnArr)
# Calculate mode
mode = stats.mode(nnArr, axis=None)

#Print values
print("Mean: {}" .format(mean))
print("Median: {}" .format(median))
#print("Mode: % s" % mode)
print(mode)
