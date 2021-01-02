# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
from sklearn.linear_model import LinearRegression as lm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# Read in the dataset
dataset = pd.read_csv(r'../Melbourne_housing_FULL.csv', skip_blank_lines=True)
dataset["Date"] = pd.to_datetime(dataset["Date"],dayfirst=True)

# Initialize arrays
dataset_dr = dataset.dropna().sort_values("Date")
dataset_dr = dataset_dr
full_Data = []

#How many days since start
days_since_start = [(x - dataset_dr["Date"].min()).days for x in dataset_dr["Date"]]
dataset_dr["Days"] = days_since_start

suburb_dummies = pd.get_dummies(dataset_dr[["Type", "Method"]])

full_Data = dataset_dr.drop(["Address", "Price", "Date", "SellerG", "Suburb", "Type", "Method", "CouncilArea", "Regionname"], axis=1).join(suburb_dummies)

X = full_Data
y = dataset_dr["Price"]

# Split into test data and training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the algorithm
regressor = lm()
regressor.fit(X_train, y_train)
print("Intercept: {}" .format(regressor.intercept_))
coeff_df = pd.DataFrame(regressor.coef_,X.columns,columns=['Coefficient'])
ranked_suburbs = coeff_df.sort_values("Coefficient", ascending = False)
print(format(ranked_suburbs, ",f"))

# Calculate linear predictions
y_pred = regressor.predict(X_test)

# Plot

plt.scatter(y_test, y_pred)
plt.ylim([200000,1000000])
plt.xlim([200000,1000000])

sns.displot((y_test-y_pred), bins=50, kde=True)
