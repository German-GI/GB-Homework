# Задание №3, сумма чисел n + nn+ nnn

n = int(input('Введите число: '))
summ = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print('Сумма чисел n + nn + nnn =',summ)