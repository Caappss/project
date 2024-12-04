def swap_columns(matrix):
    # Переставляем первый и последний столбцы
    for row in matrix:
        row[0], row[-1] = row[-1], row[0]

# Пример матрицы
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

swap_columns(matrix)

print("Матрица после перестановки столбцов:")
for row in matrix:
    print(row)