import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import csv
from scipy import stats
from sklearn.linear_model import LinearRegression

confirmed_cases = pd.read_csv('confirmedcases.csv')
states = pd.read_csv('csvData.csv')
combined = pd.merge(confirmed_cases, states, how='outer', left_on='state', right_on='State')
combined = combined.drop(['State', 'date', 'LandArea', 'WaterArea'], axis=1)
combined = combined.set_index('state')
combined = combined.drop(['fips'], axis=1)
combined['TotalArea'].fillna(0, inplace=True)
combined['Density'].fillna(0, inplace=True)
combined['Pop'].fillna(0, inplace=True)
combined = combined[combined['TotalArea'] > 0]
combined = combined[combined['Density'] > 0]
combined = combined[combined['Pop'] > 0]

x = combined['Pop']
y = combined['cases']
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print('State population vs number of confirmed cases')
print('Slope: '+str(slope))
print('Intercept: '+str(intercept))
print('Standard Error: '+str(std_err))
numpy_x = np.asarray(x).reshape(-1, 1)
numpy_y = np.asarray(y).reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(numpy_x, numpy_y)
y_pred = linear_regressor.predict(numpy_x)
plt.scatter(numpy_x, numpy_y)
plt.plot(x, y_pred, color = 'red')
plt.xlabel('State population')
plt.ylabel('Number of confimred cases')
plt.title('State population vs number of confirmed cases')
plt.show()

x_two = combined['TotalArea']
y_two = combined['cases']
slope, intercept, r_value, p_value, std_err = stats.linregress(x_two, y_two)
print('Total land area vs number of confirmed cases')
print('Slope: '+str(slope))
print('Intercept: '+str(intercept))
print('Standard Error: '+str(std_err))
numpy_x_two = np.asarray(x_two).reshape(-1, 1)
numpy_y_two = np.asarray(y_two).reshape(-1, 1)
linear_regressor_two = LinearRegression()
linear_regressor_two.fit(numpy_x_two, numpy_y_two)
y_pred_two = linear_regressor_two.predict(numpy_x_two)
plt.scatter(numpy_x_two, numpy_y_two)
plt.plot(x_two, y_pred_two, color = 'red')
plt.xlabel('Total land area')
plt.ylabel('Number of confimred cases')
plt.title('Total land area vs number of confirmed cases')
plt.show()

x_three = combined['Density']
y_three = combined['cases']
slope, intercept, r_value, p_value, std_err = stats.linregress(x_three, y_three)
print('Density vs number of confirmed cases')
print('Slope: '+str(slope))
print('Intercept: '+str(intercept))
print('Standard Error: '+str(std_err))
numpy_x_three = np.asarray(x_three).reshape(-1, 1)
numpy_y_three = np.asarray(y_three).reshape(-1, 1)
linear_regressor_three = LinearRegression()
linear_regressor_three.fit(numpy_x_three, numpy_y_three)
y_pred_three = linear_regressor_three.predict(numpy_x_three)
plt.scatter(numpy_x_three, numpy_y_three)
plt.plot(x_three, y_pred_three, color = 'red')
plt.xlabel('Density')
plt.ylabel('Number of confimred cases')
plt.title('Density vs number of confirmed cases')
plt.show()

print(combined)