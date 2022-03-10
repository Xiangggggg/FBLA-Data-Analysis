import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor

NEincomes = []
MWincomes = []
Sincomes = []
Wincomes = []
with open('neincomes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for col in csv_reader:
        num = int(col[0].replace(',','').replace('-01-01',''))
        if num >= 1974:
            NEincomes.append(int(col[1]))
with open('mwincomes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for col in csv_reader:
        num = int(col[0].replace(',','').replace('-01-01',''))
        if num >= 1974:
            MWincomes.append(int(col[1]))
with open('sincomes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for col in csv_reader:
        num = int(col[0].replace(',','').replace('-01-01',''))
        if num >= 1974:
            Wincomes.append(int(col[1]))
with open('wincomes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for col in csv_reader:
        num = int(col[0].replace(',','').replace('-01-01',''))
        if num >= 1974:
            Sincomes.append(int(col[1]))
    
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
    for i in range(len(NE)):
        NE[i] /= NEincomes[i]
        MW[i] /= MWincomes[i]
        S[i] /= Sincomes[i]
        W[i] /= Wincomes[i]

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

plt.title('Affordability of Houses in US Regions by Year')
plt.xlabel('Year')
plt.ylabel('House Price to Income Ratio')
plt.legend(loc="upper left")
plt.show()