import pandas as pd

df_vacinados = pd.read_csv('vacinados.csv')
df_vacinados = df_vacinados.sort_values('data_vacinacao',ascending=False)
print(df_vacinados.head(5))