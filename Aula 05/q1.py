frase = input("Digite uma frase: ")
palavra_alvo = input("Digite uma palavra contida na frase: ")
nova_palavra = input("Digite outra palavra para substituir a primeira: ")

frase_modificada = frase.replace(palavra_alvo, nova_palavra)
print(f"Frase modificada: {frase_modificada.upper()}")
