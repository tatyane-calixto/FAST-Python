import pandas as pd

alunos=[['Taty',8.5],
        ['Maria',9.5],
        ['João',3.5],
        ['Felipe',6.9],
        ['Roberta',7.0]]

df_alunos = pd.DataFrame(alunos,columns=['Nome','Média'])
status = ['Aprovado(a)','Aprovado(a)','Reprovado(a)','Reprovado(a)','Aprovado(a)']
df_alunos['Status'] = status

df_aprovados = df_alunos[df_alunos['Status'] == 'Reprovado(a)']
print(df_aprovados)