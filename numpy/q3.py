import numpy as np
notas= []
#usando input
for i in range (5):
    nota = float(input(f"Digite a nota{i+1}: "))
    notas.append(nota)

#converte lista em array
notas = np.array(notas)
#calcula a média
media_estudantes  = np.mean(notas[:3])
#filtra por notas acima de sete
medias_acima_sete = notas[notas>7]

#exibir
print(f"Média dos três primeiros estudantes {media_estudantes:.2f}")
print(f"Média acima de 7 {medias_acima_sete}")

