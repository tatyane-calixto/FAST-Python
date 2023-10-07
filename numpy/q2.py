import numpy as np

temperaturas  = np.array([25.0,28.0,35.0,29.0,31.5,32.6,37.0])

media_temperaturas = np.mean(temperaturas)
max_temperaturas = np.max(temperaturas)
min_temperaturas = np.min(temperaturas)

print(f"Média das temperaturas {media_temperaturas:.2f}")
print(f"Máxima das temperaturas {max_temperaturas}")
print(f"Mínima das temperaturas {min_temperaturas}")