# coding=utf-8
'''По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки'''
x1 = int(input('Введите координаты X1: '))
y1 = int(input('Введите координаты Y1: '))
x2 = int(input('Введите координаты X2: '))
y2 = int(input('Введите координаты Y2: '))

if x1 != x2 and y1 != y2 and (x2 - x1) != 0:
    k = (y2 - y1) / (x2 - x1)
    b = (x2 * y1 - x1 * y2) / (x2 - x1)
    print('Уравнение прямой y = {}x + {}'.format(k, b))
else:
    print('Уравненение составить нельзя')
