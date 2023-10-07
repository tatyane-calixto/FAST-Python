doacoes = {}

quantidade = int(input("Digite a quantidade de pessoas que desejam doar: "))

for i in range(quantidade):
    nome = input(f"Digite o nome do doador {i + 1}: ")
    valor = float(input(f"Digite o valor da doação de {nome}: "))
    doacoes[nome] = valor

total_doacoes = sum(doacoes.values())


print("\nDicionário de doações:")
for nome, valor in doacoes.items():
    print(f"{nome}: R${valor:.2f}")

print(f"\nTotal em doações arrecadado: R${total_doacoes:.2f}")
