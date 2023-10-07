import pandas as pd

estados_nordeste = {
    'Estado': ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe'],
    'Sigla': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
    'População': ['3,4 milhões', '15,4 milhões', '9,2 milhões', '7,1 milhões', '4,0 milhões', '9,7 milhões', '3,3 milhões', '3,5 milhões', '2,3 milhões'],
    'Capital': ['Maceió', 'Salvador', 'Fortaleza', 'São Luís', 'João Pessoa', 'Recife', 'Teresina', 'Natal', 'Aracaju']
}
df = pd.DataFrame(estados_nordeste)
print(df.iloc[2:5, 0:2])
