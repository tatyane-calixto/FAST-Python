import pandas as pd

estados=['Maranhão (MA)', 
        'Piauí (PI)',
        'Ceará (CE)', 
        'Rio Grande do Norte (RN)', 
        'Paraíba (PB)', 
        'Pernambuco (PE)', 
        'Alagoas (AL)', 
        'Sergipe (SE)',
        'Bahia (BA)']

# Criando um DataFrame com uma coluna nomeada 'Estados'
df = pd.DataFrame(estados)

print(df)
