# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# Read in the dataset
dataset = pd.read_csv(r'../Melbourne_housing_FULL.csv', skip_blank_lines=True)

# Initialize arrays
df = dataset[["Rooms", "Bathroom"]].dropna()
x = df.iloc[:, :-1].values
y = df.iloc[:, 1].values

# Split into test data and training data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Train the algorithm
regressor = LinearRegression()
regressor.fit(x_train, y_train)
print("Intercept: {}" .format(regressor.intercept_))
print("Change in every step: {}" .format(regressor.coef_))

# Calculate linear predictions
y_pred = regressor.predict(x_test)

newframe = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
newframe

# Calculate polynomial predictions
poly_reg = PolynomialFeatures()
x_poly = poly_reg.fit_transform(x)
pol_reg = LinearRegression()
pol_reg.fit(x_poly, y)

# Plot
def linear_plot():
    plt.scatter(x, y)
    plt.plot(x_test, y_pred, color='red')
    plt.ylabel("Number of bathrooms")
    plt.xlabel("Number of rooms")
    plt.title("Linear regression bathrooms-rooms")
    plt.show()

def poly_plot():
    plt.scatter(x, y)
    plt.plot(x, pol_reg.predict(poly_reg.fit_transform(x)), color='blue')
    plt.ylabel("Number of bathrooms")
    plt.xlabel("Number of rooms")
    plt.title("Polynomial regression bathrooms-rooms")
    plt.show()
