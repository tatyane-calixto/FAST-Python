level = int(input('Digite o level do Voltorb: '))

if level >=1 and level <=20:
    potencia = 20 + level**3
elif level >=21 and level <=40:
    potencia = 800 + (level-10)**2
elif level >=41 and level <=60: 
    potencia = 9000 + 5*level
elif level >=61 and level <=80:
    potencia = 9300 + 2*level
elif level >=81 and level <=100:
    potencia = 9500 + level
else:
    print("Valor inválido!")

print(f"A potência é de {potencia}")