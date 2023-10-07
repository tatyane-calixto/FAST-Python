import pandas as pd
data = {
    'Produto': ['Smartphone', 'Laptop', 'Tablet', 'Fone de Ouvido', 'Smart TV'],
    'Qtd_Vendida': [100, 50, 80, 120, 30],
    'Preco_Unitario': [800, 2500, 600, 80, 1800]
}
df_dados = pd.DataFrame(data)
df_dados['Receita'] = df_dados['Qtd_Vendida'] * df_dados['Preco_Unitario']
printdf_dados = df_dados['Qtd_Vendida']>80
