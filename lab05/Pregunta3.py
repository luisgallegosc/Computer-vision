import numpy as np

# Definir la matriz original
original_matrix = np.array([[0, 1, 2],
                            [3, 4, 5],
                            [6, 7, 8]])

scale_factor = 3
rows, cols = original_matrix.shape
new_rows, new_cols = rows * scale_factor, cols * scale_factor
scaled_matrix = np.zeros((new_rows, new_cols), dtype=int)

for i in range(new_rows):
    for j in range(new_cols):
        original_i, original_j = i // scale_factor, j // scale_factor
        scaled_matrix[i, j] = original_matrix[original_i, original_j]

#mostrar la matriz original
print("Matriz Original:")
print(original_matrix)

#mostrar la matriz escalada
print("\nMatriz Escalada:")
print(scaled_matrix)
