# Import libraries
import pandas as pd
import math
import numpy
from scipy import stats
import statistics

# Read in the dataset
dataset = pd.read_csv(r'../Melbourne_housing_FULL.csv', skip_blank_lines=True)

nnArr = []

# Disregard null values
for p in dataset.Bathroom:
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

#----------------------------------

#Variability - Range
statrange = numpy.ptp(nnArr)
#Variability - Interquartile Range
q3, q1 = numpy.percentile(nnArr, [75, 25])
iqr = q3 - q1
#Variability - Variance
variance = statistics.variance(nnArr)
#Variance - Standard Deviation
stddeviation = numpy.std(nnArr, ddof=1)

#Print values
print("Mean: {}" .format(mean))
print("Median: {}" .format(median))
print(mode)
print("\nRange: {}" .format(statrange))
print("IQR: {}" .format(iqr))
print("Variance: {}" .format(variance))
print("Standard deviation: {}" .format(stddeviation))
