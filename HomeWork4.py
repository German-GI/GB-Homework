# Задание №4, нахождение самой большой цифры в введённом чсисле
number = abs(int(input('Введите целое положительное число ')))
if number > 0:
    max_number = number % 10
    while number >= 1:
        number = number // 10
        if number % 10 > max_number:
            max_number = number % 10
        if number > 9:
            continue
        else:
            print('Максимальное цифра в числе ', max_number)
            break
else:
    print('вы ввели отрицательное число или оно равно 0')