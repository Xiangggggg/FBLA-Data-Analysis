import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor

with open('7.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    columns = []
    for row in csv_reader: 
        columns.append(row)
        break
    columns = columns[0]
    x = []
    x2 = []
    y = []
    for col in csv_reader:
        num = int(col[2].replace(',',''))
        x.append([int(col[0])])
        x2.append(int(col[0]))
        y.append(num)

    regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
    regressor.fit(x, y)
    Y_pred = regressor.predict(np.array([6.5]).reshape(1, 1)) 
    X_grid = np.arange(min(x2), max(x2), 0.01)
    
    # reshape for reshaping the data into a len(X_grid)*1 array,
    # i.e. to make a column out of the X_grid value                 
    X_grid = X_grid.reshape((len(X_grid), 1))
    

    
    # Scatter plot for original data
    plt.scatter(x, y, color = 'blue') 
    
    # plot predicted data
    plt.plot(X_grid, regressor.predict(X_grid),
            color = 'green')
    plt.title('Median Price of Houses Sold in North-Eastern US by Year')
    plt.xlabel('Year')
    plt.ylabel('Median price of Houses Sold')
    plt.show()
