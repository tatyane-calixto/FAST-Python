import pandas as pd

data = {
    'A': [10, 20, 30, 40],
    'B': [5, 15, 25, 35],
    'C': [2, 4, 6, 8]
}

df = pd.DataFrame(data)

soma_A = df['A'].sum()
soma_B = df['B'].sum()
soma_C = df['C'].sum()

print(soma_C)