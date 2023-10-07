a = []
b = []

for i in range(5):
    a = int(input("Digite valor da lista a"))
    a.append(a)
    b = int(input("Digite valor da lista b"))
    b.append(b)

c = a+b
soma_pares = 0
media_impares = 0
soma_impares = 0
qtd_impares = 0


for final in c:
    if final % 2 ==0:
        soma_pares+=final
    else:
        qtd_impares+=1
        soma_impares+=final

print(f"Soma dos números pares {soma_pares}")
print(f"Média dos  números ímpares {soma_impares/qtd_impares}")
print(f"Menor número da lista: {min(c)}")