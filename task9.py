# coding=utf-8
'''Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)'''
a = raw_input('Введите первое число: ')
b = raw_input('Введите второе число: ')
c = raw_input('Введите третье число: ')

try:
    a = float(a)
    b = float(b)
    c = float(c)
    if c <= a <= b or b <= a <= c:
        print('Среднее число равно: {} '.format(a))
    elif c <= b <= a or a <= b <= c:
        print('Среднее число равно: {} '.format(b))
    else:
        print('Среднее число равно: {} '.format(c))
except ValueError:
    print ('Ошибка ввода данных')
