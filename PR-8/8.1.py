def is_magic_square(matrix): # Определяет функцию is_magic_square
    n = len(matrix) # Вычисляем размерность функции len(), которая возвращает количество строк в матрице
    magic_sum = sum(matrix[0])  # Сумма первой строки

    # Проверка сумм строк
    for row in matrix:
        if sum(row) != magic_sum:
            return False # Мы проходим по каждой строке row, Если сумма не равна magic_sum, функция немедленно возвращает False

    # Проверка сумм столбцов
    for col in range(n): # Здесь мы проверяем суммы столбцов. Мы используем цикл for, чтобы пройти по каждому индексу столбца от 0 до n-1
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False

    return True # Если все проверки пройдены, функция возвращает True

# Пример использования
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
] #Здесь мы создаем пример магического квадрата размером 3x3

if is_magic_square(matrix):
    print("Это магический квадрат.")
else:
    print("Это не магический квадрат.")