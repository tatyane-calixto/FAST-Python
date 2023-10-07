medicoes = []
for i in range(10):
    medicao = float(input(f"Digite a medição {i + 1}: "))
    medicoes.append(medicao)

# Abre o arquivo para escrever
arquivo = open('medicoes.txt', 'w')
for medicao in medicoes:
    arquivo.write(str(medicao) + '\n')
arquivo.close()  # Fecha o arquivo após escrever os dados

contagem = 0

# Abre o arquivo para leitura
arquivo = open('medicoes.txt', 'r')
linhas = arquivo.readlines()
arquivo.close()  # Fecha o arquivo após ler os dados

for i in range(1, len(linhas)):
    mediacao_atual = float(linhas[i])
    mediacao_anterior = float(linhas[i - 1])

    if mediacao_atual > mediacao_anterior:
        contagem += 1

print(f"Quantidade de medições maiores que a anterior: {contagem}")
