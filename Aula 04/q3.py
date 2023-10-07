idades = []
for i in range(4):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    idades.append(idade)

print("\nIdades armazenadas:", idades)

media_idades = sum(idades) / len(idades)

maior_idade = max(idades)
menor_idade = min(idades)

print(f"Média das idades: {media_idades:.2f}")
print(f"Maior idade: {maior_idade}")
print(f"Menor idade: {menor_idade}")
