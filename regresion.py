## ejemplo de regresion con datos de quandl para oracle
## API KEY quandl -> oKwYeLxg3fyRASCagzVs
 
import pandas as pd 
import quandl
import matplotlib.pyplot as plt

df = quandl.get("GOOG/NASDAQ_ORCL")
data = quandl.Dataset('GOOG/NASDAQ_ORCL').data()
prom_hist = 0

df = df [[ 'High' , 'Low' ,'Open','Close' ]]

df['Volat'] = (df['High'] - df['Close']) /  df['Close'] * 100.0
df['Porc_Cambio'] = (df['Close'] - df['Open']) /  df['Open'] * 100.0

df = df [[ 'Close' , 'Volat' ,'Porc_Cambio']]

print(df)
print()

dat = []
tot = 0

for e in data:
    v = float(e.close or 0)
    prom_hist += v #los valores que no se tengan se vuelven cero
    dat.append(v) if v != 0 else v
    tot += 1 if v != 0 else v

prom_hist = prom_hist / tot
print("El promedio historico de las acciones de Oracle es de : ", prom_hist)

plt.plot([dat], color = 'r')
plt.show()