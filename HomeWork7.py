# Задание №7 Расчёт эффективности тренеровки спортсмена
a = float(input('Введите результаты пробежки первого дня в км '))
b = float(input('Введите желаемый результат в км '))
day = 1
while a < b:
    print(day, '-й день, расстояние =', a)
    a += 0.1
    day = day + 1
print('Лёгких тренеровок')