n = int(input("digite quantos minutos faltam: "))
tempo_p1 = int(input("Digite o tempo do presente 1: "))
tempo_p2 = int(input("Digite o tempo do presente 2: "))
tempo_presente= tempo_p1 + tempo_p2

if tempo_presente <= n:
    print('Farei hoje!')
else:
    print('Deixa para amanhã!')