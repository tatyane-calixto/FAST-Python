import pandas as pd

estados_nordeste = [['Alagoas', 'AL', '3,4 milhões', 'Maceió'],
                    ['Bahia', 'BA', '15,4 milhões', 'Salvador'],
                    ['Ceará', 'CE', '9,2 milhões', 'Fortaleza'],
                    ['Maranhão', 'MA', '7,1 milhões', 'São Luís'],
                    ['Paraíba', 'PB', '4,0 milhões', 'João Pessoa'],
                    ['Pernambuco', 'PE', '9,7 milhões', 'Recife'],
                    ['Piauí', 'PI', '3,3 milhões', 'Teresina'],
                    ['Rio Grande do Norte', 'RN', '3,5 milhões', 'Natal'],
                    ['Sergipe', 'SE', '2,3 milhões', 'Aracaju']]

# Criando o DataFrame com as colunas nomeadas
df = pd.DataFrame(estados_nordeste, columns=['Estado', 'Sigla', 'População', 'Capital'])

print(df)
