def reverse_number(num):
    # Преобразуем число в строку, переворачиваем и возвращаем обратно в целое число
    return int(str(num)[::-1])

# Пример использования
number = 12345
reversed_number = reverse_number(number)

print("Исходное число:", number)
print("Число в обратном порядке:", reversed_number)