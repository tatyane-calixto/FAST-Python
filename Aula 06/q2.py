def  imprimir(numero):
    numeros = ""
    for i in range (1,numero+1):
        numeros+= str(i) + " "
    print (numeros)

def sequencia():
    while True:
        numero = int(input("Digite um número: "))
        if(numero==0):
            break
        else:
            imprimir(numero)

sequencia()