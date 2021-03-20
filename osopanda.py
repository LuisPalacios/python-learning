#
import pandas as p

fichero = "la-liga-2019.csv"
df = p.read_csv(fichero)

print(df.tail())

df.head()

newdf = df["Home Team"]

print(newdf.head())


