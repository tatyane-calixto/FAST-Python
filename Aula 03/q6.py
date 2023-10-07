numero = int(input("Digite um número: "))
n = 0
triangulo = False
for i in range (numero):
    n+=i
    if n == numero:
        triangulo = True
        break

if triangulo:
    print("triangular")
else: 
    print("Não triangular")


