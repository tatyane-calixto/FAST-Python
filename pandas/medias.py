import pandas as pd

data = {
    'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eva'],
    'Nota1': [8.5, 7.8, 9.2, 6.5, 5.9],
    'Nota2': [6.0, 1.2, 9.2, 6.5, 10]
}
 
df_estudantes = pd.DataFrame(data)
df_estudantes['Media'] = df_estudantes[['Nota1', 'Nota2']].mean(axis=1)
df_aprovados = df_estudantes[df_estudantes['Media'] >= 7]
print(df_aprovados[['Nome', 'Media']])

