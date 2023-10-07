def escrever_nomes_arquivo(nomes, nome_arquivo):
    with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
        for nome in nomes:
            arquivo.write(nome + '\n')


nomes = []
for i in range(6):
    nome = input("Digite o nome: ")
    nomes.append(nome)

arquivo_original = "nomes.txt"
arquivo_ordenado = "nomes_ordenados.txt"


escrever_nomes_arquivo(nomes, arquivo_original)

nomes.sort()
escrever_nomes_arquivo(nomes, arquivo_ordenado)
print("Nomes foram ordenados e salvos em 'nomes_ordenados.txt'.")
