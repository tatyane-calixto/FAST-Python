corredores = {}


for i in range(5):
    nome = input(f"Digite o nome do corredor {i + 1}: ")
    tempos = []
    for j in range(3):
        tempo = float(input(f"Digite o tempo da volta {j + 1} em minutos: "))
        tempos.append(tempo)
    corredores[nome] = tempos


medias = {}
for nome, tempos in corredores.items():
    media = sum(tempos) / 3
    medias[nome] = round(media, 3)


melhor_corredor = min(medias, key=medias.get)


print("\nMédia de tempo de cada corredor:")
for nome, media in medias.items():
    print(f"{nome}: {media} minutos")

print(f"\nO corredor com a menor média é {melhor_corredor.upper()} com média {medias[melhor_corredor]} minutos.")
