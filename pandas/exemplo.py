import pandas as pd

df_pokemon = pd.read_csv('pokemon.csv')
df_pokemon1 = df_pokemon.loc[df_pokemon['Attack'] > 100 & (df_pokemon['Defense'] > 80)]
print(df_pokemon1['Name'])