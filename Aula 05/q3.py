palavra = input("Digite o nome: ")
letras = []

for letra in palavra:
    letras.append(letra)

letra = ""

for i in range (len(letras)):
    letra= letra + letras[i]
    print(letra.upper())