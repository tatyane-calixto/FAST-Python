import pandas as pd

data = {
    'Produto': ['Smartphone', 'Laptop', 'Tablet', 'Fone de Ouvido', 'Smart TV'],
    'Qtd_Vendida': [100, 50, 80, 120, 30],
    'Preco_Unitario': [800, 2500, 600, 80, 1800]
}

df_produtos = pd.DataFrame(data)

df_produtos['Receita'] = df_produtos['Qtd_Vendida'] * df_produtos['Preco_Unitario']
produtos_mais_vendidos = df_produtos[df_produtos['Qtd_Vendida'] > 80]
print(produtos_mais_vendidos )
