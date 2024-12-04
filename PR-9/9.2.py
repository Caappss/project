def second_largest():
    largest = None
    second_largest = None

    while True:
        num = int(input("Введите натуральное число (0 для завершения): "))
        if num == 0:
            break

        # Обновляем значения largest и second_largest
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or (num > second_largest and num < largest):
            second_largest = num

    if second_largest is not None:
        print("Второй по величине элемент:", second_largest)
    else:
        print("Не было введено достаточно чисел.")


# Запуск функции
second_largest()