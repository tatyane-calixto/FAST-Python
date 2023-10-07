#código de Paloma Freire
import numpy as np

vendas = []
for i in range(5):
    valor_vendas = float(input(f'Qual o valor das vendas de hoje {i+1}: '))
    vendas.append(valor_vendas)

#converte lista em array
vendas = np.array(vendas)
media_vendas = np.mean(vendas[:5])

media_acima_mil = vendas[vendas > 1000]

print(vendas)
print(media_vendas)
print(media_acima_mil)