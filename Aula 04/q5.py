quantidade_mouses = int(input("Digite a quantidade de mouses: "))


necessita_esfera = 0
necessita_limpeza = 0
troca_cabo_conector = 0
quebrado_inutilizado = 0


for i in range(quantidade_mouses):
    num_identificacao = input(f"Digite o número de identificação do mouse {i + 1}: ")
    defeito = input(f"Digite o tipo de defeito do mouse {i + 1} (opções: necessita da esfera, necessita de limpeza, necessita troca do cabo ou conector, quebrado ou inutilizado): ")
    
    if defeito == 'necessita da esfera':
        necessita_esfera += 1
    elif defeito == 'necessita de limpeza':
        necessita_limpeza += 1
    elif defeito == 'necessita troca do cabo ou conector':
        troca_cabo_conector += 1
    elif defeito == 'quebrado ou inutilizado':
        quebrado_inutilizado += 1
    else:
        print(f"Tipo de defeito inválido para o mouse {i + 1}. O mouse não será registrado.")


total_mouses = quantidade_mouses
percentual_esfera = (necessita_esfera / total_mouses) * 100
percentual_limpeza = (necessita_limpeza / total_mouses) * 100
percentual_troca = (troca_cabo_conector / total_mouses) * 100
percentual_quebrado = (quebrado_inutilizado / total_mouses) * 100


print("\nRelatório de mouses:")
print(f"Quantidade de mouses: {total_mouses}")
print("Situação:")
print(f"1. necessita da esfera; {necessita_esfera}")
print(f"2. necessita de limpeza; {necessita_limpeza}")
print(f"3. necessita troca do cabo ou conector; {troca_cabo_conector}")
print(f"4. quebrado ou inutilizado; {quebrado_inutilizado}")
print("Percentual:")
print(f"{percentual_esfera:.2f}%")
print(f"{percentual_limpeza:.2f}%")
print(f"{percentual_troca:.2f}%")
print(f"{percentual_quebrado:.2f}%")
