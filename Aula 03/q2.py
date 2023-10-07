feminino = 0
cabelos_olhos = 0

for i in range(5):
    sexo = input("Digite o sexo: ")
    idade = int(input("Digite a idade: "))
    olhos = input("Digite a cor dos olhos: ")
    cabelos = input("Digite a cor dos cabelos: ")

    if sexo == "F" and 18<=idade<=35:
        feminino+=1
    
    if olhos == "castanhos" and cabelos =="pretos":
        cabelos_olhos+=1

print(f"Quantidade de pessoas do sexo Feminino entre 18 e 35 anos {feminino}")
print(f"Quantidade de pessoas de olhos castanhos e cabelos pretos {cabelos_olhos}")