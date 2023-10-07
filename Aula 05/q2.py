# Abra o arquivo para escrita, criando-o se não existir
with open('medicoes.txt', 'w') as arquivo:
    # Solicite ao usuário que insira 10 valores de medições
    for i in range(7):
        medição = input(f"Digite o valor da medição {i + 1}: ")
        arquivo.write(medição + '\n')

# Abra o arquivo para leitura
with open('medicoes.txt', 'r') as arquivo:
    # Leia todas as linhas do arquivo em uma lista
    linhas = arquivo.readlines()

# Inicialize uma variável para contar as medições maiores que a anterior
contagem = 0

# Itere pelas linhas do arquivo a partir da segunda linha (índice 1)
for i in range(1, len(linhas)):
    # Converta o valor atual e o valor anterior para números inteiros
    valor_atual = int(linhas[i])
    valor_anterior = int(linhas[i - 1])
    
    # Verifique se a medição atual é maior que a anterior
    if valor_atual > valor_anterior:
        contagem += 1

# Exiba o resultado
print(f"Quantidade de medições maiores que a anterior: {contagem}")
