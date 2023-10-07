# Dicionário para armazenar os tempos de corrida dos corredores
corredores = {}

# Receber o nome e os tempos de três voltas de cinco corredores
for i in range(3):
    nome = input(f"Digite o nome do corredor {i + 1}: ")
    tempos = []
    for j in range(3):
        tempo = float(input(f"Digite o tempo da volta {j + 1} em minutos: "))
        tempos.append(tempo)
    corredores[nome] = tempos

# Calcular a média de tempo de cada corredor e encontrar o melhor corredor
melhor_corredor = None
melhor_media = 0

print("\nMédia de tempo de cada corredor:")
for nome, tempos in corredores.items():
    media = sum(tempos) / 3
    media = round(media, 3)
    print(f"{nome}: {media} minutos")
    
    if media < melhor_media:
        melhor_media = media
        melhor_corredor = nome
print(melhor_media,melhor_corredor)

print(f"O corredor com a menor média é {melhor_corredor.upper()} com média {melhor_media} minutos.")
7