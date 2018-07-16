# coding=utf-8
'''Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.'''
alph = 'abcdefghijklmnopqrstuvwxyz'
import random
from random import randint, uniform, choice

a = raw_input('Введите первую границу случайного целого числа:')
b = raw_input('Введите вторую границу случайного целого числа:')
try:
    a = int(a)
    b = int(b)

    if a <= b:
        print('Случайное число: {}'.format(random.randint(a, b)))
    else:
        print('Случайное число: {}'.format(random.randint(b, a)))

except ValueError:
    print('Ошибка ввода данных')

a = raw_input('Введите первую границу случайного вещественного числа:')
b = raw_input('Введите вторую границу случайного вещественного числа:')
try:
    a = float(a)
    b = float(b)

    if a <= b:
        print(random.uniform(a, b))
    else:
        print(random.uniform(b, c))

except ValueError:
    print('Ошибка ввода данных')

a = raw_input('Введите первую букву:')
b = raw_input('Введите вторую букву:')

if a in alph and b in alph:
    a = alph.index(a)
    b = alph.index(b)
    if a < b:
        print('Случайный симвом из диапазона [{}:{}] - {}'.format(alph[a], alph[b], random.choice(alph[a:b])))
    elif b > a:
        print('Случайный симвом из диапазона [{}:{}] - {}'.format(alph[b], alph[a], random.choice(alph[b:a])))
    else:
        print('Случайный симвом из диапазона [{}:{}] - {}'.format(alph[a], alph[a], alph[a]))

else:
    print ('Ошибка ввода данных')
