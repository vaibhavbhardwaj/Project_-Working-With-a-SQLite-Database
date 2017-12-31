import sqlite3
import pandas as pd
import math
conn = sqlite3.connect("factbook.db")
query = "select * from facts;"
df = pd.read_sql_query(query,conn)
df = df[1:]
print(df.columns)
df.dropna()

df = df[df["area_land"] == 0]

def new_population(data):
    growth_rate = data["population_growth"]
    population = data["population"]
    new_p = population * math.e**((growth_rate/100) *35)
    return (new_p)
df['new population'] = df.apply(new_population,axis=1)
print(df.sort_values("new population",ascending=False).head(10))