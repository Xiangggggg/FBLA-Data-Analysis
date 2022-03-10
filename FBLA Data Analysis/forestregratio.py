import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor

location = 5
with open('7.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    x = []
    x2 = []
    y = []
    for col in csv_reader:
        if int(col[0]) >= 1974:
            num = int(col[location].replace(',',''))
            x.append([int(col[0])])
            x2.append(int(col[0]))
            y.append(num)
with open('wincomes.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',')
    years = []
    years2 = []
    incomes = []
    for col in csv_reader:
        num = int(col[0].replace(',','').replace('-01-01',''))
        if num >= 1974:
            years.append([num])
            years2.append(num)
            incomes.append(int(col[1]))

with open('1.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',')
    sales = []
    for col in csv_reader:
        if int(col[0]) >= 1974:
            num = int(col[location])
            sales.append(num)

for i in range(len(y)):
    y[i] /= incomes[i]

regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
regressor.fit(x, y)
X_grid = np.arange(min(x2), max(x2), 0.05)                 
X_grid = X_grid.reshape((len(X_grid), 1))

color = 'tab:blue'
fig, ax1 = plt.subplots()
# Scatter plot for original data
ax1.scatter(x, y, color = color) 

# plot predicted data
ax1.plot(X_grid, regressor.predict(X_grid),
        color = color)

ax1.set_xlabel('Year')
ax1.set_ylabel('House Price-Income Ratio',color=color)
ax1.tick_params(axis='y',labelcolor=color)

regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
regressor.fit(x, sales)

color2 = 'tab:red'
ax2 = ax1.twinx()
ax2.set_ylabel('Houses Sold in Thousands',color=color2)
ax2.tick_params(axis='y',labelcolor=color2)
ax2.plot(X_grid, regressor.predict(X_grid),
        color = color2)
ax2.scatter(x, sales, color=color2) 
plt.title('House Price-Income Ratio and Houses Sold by Year in Western US')

fig.tight_layout()
plt.show()
