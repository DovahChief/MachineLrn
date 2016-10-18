import pandas as pd 
import quandl , math
import numpy as np
from sklearn import preprocessing , cross_validation , svm
from sklearn.linear_model import LinearRegression

### para acciones de google 

quandl.ApiConfig.api_key = "oKwYeLxg3fyRASCagzVs"


df = quandl.get("WIKI/GOOGL")
df = df[['Adj. Open', 'Adj. High', 'Adj. Low' , 'Adj. Close' , 'Adj. Volume']]

df['Volat'] = (df['Adj. High'] - df['Adj. Close']) /  df['Adj. Close'] * 100.0
df['Porc_Cambio'] = (df['Adj. Close'] - df['Adj. Open']) /  df['Adj. Open'] * 100.0

df = df[ ['Adj. Close', 'Volat', 'Porc_Cambio', 'Adj. Volume'] ]

pronostico_c = 'Adj. Close'
df.fillna(-99999 , inplace=True)

pronostico_sal = int(math.ceil(0.01*len(df)))

df['label'] = df[pronostico_c].shift(-pronostico_sal)
df.dropna(inplace=True)


X = np.array(df.drop(['label'] ,1)) #quita la columna label y la regresa
y = np.array(df['label'])           # solo saca la columna label
X = preprocessing.scale(X)

x_train , x_test , y_train , y_test  = cross_validation.train_test_split(X,y, test_size = 0.2)

clf = LinearRegression()

clf.fit(x_train, y_train)

precision = clf.score(x_test, y_test)

print(precision)