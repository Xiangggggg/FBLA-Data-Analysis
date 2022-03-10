import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor

with open('7.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    x = []
    x2 = []
    NE = []
    MW = []
    S = []
    W = []
    for col in csv_reader:
        num = int(col[0])
        if num >= 1974:
            x.append([num])
            x2.append(num)
            NE.append(int(col[2].replace(',','')))
            MW.append(int(col[3].replace(',','')))
            S.append(int(col[4].replace(',','')))
            W.append(int(col[5].replace(',','')))
   
    X_grid = np.arange(min(x2), max(x2), 0.01)
                    
    X_grid = X_grid.reshape((len(X_grid), 1))

    color = 'blue'
    regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
    regressor.fit(x, NE)
    plt.scatter(x, NE, color = color)  
    plt.plot(X_grid, regressor.predict(X_grid),color = color,label="North-Eastern")

    color = 'red'
    regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
    regressor.fit(x, MW)
    plt.scatter(x, MW, color = color)  
    plt.plot(X_grid, regressor.predict(X_grid),color = color,label="Mid-Western")

    color = 'green'
    regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
    regressor.fit(x, S)
    plt.scatter(x, S, color = color)  
    plt.plot(X_grid, regressor.predict(X_grid),color = color,label="Southern")

    color = 'orange'
    regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
    regressor.fit(x, W)
    plt.scatter(x, W, color = color)  
    plt.plot(X_grid, regressor.predict(X_grid),color = color,label="Western")

plt.title('Median Prices of Houses Sold in US Regions by Year')
plt.xlabel('Year')
plt.ylabel('Median Price of House Sold')
plt.legend(loc="upper left")
plt.show()
