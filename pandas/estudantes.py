import pandas as pd

data = {
    'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eva'],
    'Média': [8.5, 7.8, 9.2, 6.5, 5.9]
}
 
df_estudantes = pd.DataFrame(data)

status = ['Aprovado','Aprovado','Aprovado','Reprovado','Reprovado']

df_estudantes['Status'] = status

df_aprovados = df_estudantes[df_estudantes['Status'] == 'Reprovado']
print(df_aprovados)

