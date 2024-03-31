import numpy as np

# Inicializar la matriz inicial de la imagen
n = 3
matrizInicial = np.array([[0,1,2],
                          [3,4,5],
                          [6,7,8]], dtype=np.uint8)

# inicializar la matriz requerida
matrizInterpolada = []
for i in range(2*n):
    newRow = []
    for j in range(2*n):
        newRow.append(-1)
    matrizInterpolada.append(newRow)

# LLenar los elementos faltantes usando el criterio de 
# interpolacion para el vecino mas cercano
for i in range(n):
    for j in range(n):
        matrizInterpolada[2*i][2*j] = matrizInicial[i][j]
        matrizInterpolada[2*i][2*j+1] = matrizInicial[i][j]
        matrizInterpolada[2*i+1][2*j] = matrizInicial[i][j]
        matrizInterpolada[2*i+1][2*j+1] = matrizInicial[i][j]

matrizRequerida = np.array(matrizInterpolada)

# Mostrar la matriz final
print(matrizRequerida)