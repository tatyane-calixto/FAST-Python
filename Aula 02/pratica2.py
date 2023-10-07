nome = input("Digite o nome do(a) cliente: ")
sexo =input("Digite o sexo do(a) cliente (F ou M): ")
valor_compra = float(input("Digite o valor da compra: "))

if sexo == "F":
    desconto = valor_compra * 0.13
else:
    desconto = valor_compra * 0.05

total_pagar = valor_compra - desconto

print(f"Cliente {nome}")
print(f"Valor da compra R$ {valor_compra}")
print(f"Desconto {desconto}")
print(f"Valor a pagar R$ {total_pagar}")
