"""
Simulação da Malha Vetorial 2D com Compressão Gravitacional Central
Baseado no postulado vetorial: ω(x, y) · ε₋(x, y) = -1
Autor: Charles de Paula Eugênio
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parâmetros da malha
grid_size = 100
omega = np.ones((grid_size, grid_size))  # Frequência angular ω(x, y)
epsilon = -1 * np.ones((grid_size, grid_size))  # Resistência vetorial ε₋(x, y)

# Função de compressão gravitacional centrada (distribuição gaussiana)
def compressao_gravitacional(x, y, sigma=10):
    cx, cy = grid_size // 2, grid_size // 2
    return np.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * sigma ** 2))

# Aplicar variação gaussiana de compressão à frequência angular ω
for i in range(grid_size):
    for j in range(grid_size):
        omega[i, j] += 0.5 * compressao_gravitacional(i, j)

# Calcular tensão vetorial τ(x, y) = ω(x, y) * ε₋(x, y)
tensao = omega * epsilon

# Visualização do campo de tensão (mapa de calor)
plt.figure(figsize=(8, 6))
plt.imshow(tensao, cmap='viridis')
plt.colorbar(label='Tensão Vetorial τ(x, y)')
plt.title('Simulação da Malha Vetorial 2D com Compressão Central')
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.savefig('malha_vetorial_2d.png')
plt.close()

# Exportar matriz de tensões para CSV
df = pd.DataFrame(tensao)
df.to_csv('malha_vetorial_2d.csv', index=False)

print("Simulação concluída.")
print("Arquivos gerados: malha_vetorial_2d.csv e malha_vetorial_2d.png")
