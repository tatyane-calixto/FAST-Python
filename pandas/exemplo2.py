import pandas as pd

df_pokemon = pd.read_csv('pokemon.csv')
df_pokemon = df_pokemon.sort_values(['Type 1','Name'])
print(df_pokemon.head(10)[['Name','Type 1']])