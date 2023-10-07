import pandas as pd

df_pokemon = pd.read_csv('pokemon.csv')
# criar coluna total e somando os valores
df_pokemon['total'] = df_pokemon['HP'] + df_pokemon['Attack']+df_pokemon['Defense']+df_pokemon['Sp. Atk']+df_pokemon['Sp. Def']+df_pokemon['Speed']
df_pokemon = df_pokemon[['Name','total']]
# exibe o total do maior para o menor
print(df_pokemon.sort_values('Name',ascending=False))