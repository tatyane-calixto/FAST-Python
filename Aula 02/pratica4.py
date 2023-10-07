consumo = float(input("Digite o valor do consumo: "))

if consumo <=500:
    print("O valor da conta é R$ ", consumo*0.02+5)
elif consumo > 500 and consumo<=1000:
    print("O valor da conta é R$ ", consumo*10+5)
else:
    print("O valor da conta é R$ ",consumo*35+5)