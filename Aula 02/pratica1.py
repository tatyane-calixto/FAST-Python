velocidade = float(input("Qual é a velocidade em km/h?"))

if velocidade > 80:
    velocidade_passou  = velocidade - 80
    multa = velocidade_passou * 5
    print("Você foi multado(a)")
    print(f"O valor da multa é R$ {multa:.2f}")