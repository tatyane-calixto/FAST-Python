def horas_para_minutos(horas):
    minutos = horas * 60
    return minutos

def horas_para_segundos(horas):
    segundos = horas * 3600
    return segundos
  
  
horas = float(input("Digite um valor em horas: "))
escolha = input("Escolha a opção (minutos/segundos): ").lower()
if horas > 0:
    if escolha == "minutos":
        minutos = horas_para_minutos(horas)
        print(f"{horas} horas equivalem a {minutos} minutos.")
    elif escolha == "segundos":
        segundos = horas_para_segundos(horas)
        print(f"{horas} horas equivalem a {segundos} segundos.")
    else:
        print("Opção inválida. Por favor, escolha 'minutos' ou 'segundos'.")
else:
    print("O valor das horas não pode ser negativo")

