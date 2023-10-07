estado_civil = input("Digite o estado civil: ")

if estado_civil == "S":
    print("Pessoa Solteira!")
elif estado_civil == "C":
    print("Pessoa Casada!")
elif estado_civil == "V":
    print("Pessoa Viúva!")
elif estado_civil == "D":
    print("Pessoa Divorciada!")
else:
    print("Estado Civil inválido")