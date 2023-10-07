medicoes = []
for i in range(10):
    medicao = float(input(f"Digite a medição {i + 1}: "))
    medicoes.append(medicao)


with open('medicoes.txt', 'w') as arquivo:
    for medicao in medicoes:
        arquivo.write(str(medicao) + '\n')


contagem = 0


with open('medicoes.txt', 'r') as arquivo:
    
    linhas = arquivo.readlines()


for i in range(1, len(linhas)):
    
    mediacao_atual = float(linhas[i])
    mediacao_anterior = float(linhas[i - 1])

    
    if mediacao_atual > mediacao_anterior:
        contagem += 1


print(f"Quantidade de medições maiores que a anterior: {contagem}")
