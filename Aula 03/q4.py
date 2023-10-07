numero = int(input("Digite o número da tabuada: "))
inicio = int(input("Digite o número do inicio da tabuada: "))
fim = int(input("Digite o número do final da tabuada: "))

for i in range(inicio, fim+1):
    resultado = numero * i
    print(f"{numero}x {i} = {resultado}")