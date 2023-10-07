import pandas as pd

dados_alunos = []

for i in range(3):
    nome = input("Insira o nome do aluno: ")
    disciplina = input("Insira a Disciplina: ")
    nota = float(input("Insira a nota1 do aluno: "))
    dados_alunos.append({'Nome': nome, 'Disciplina': disciplina, 'Nota': nota})

df = pd.DataFrame(dados_alunos)
print(df)
