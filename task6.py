# coding=utf-8
'''Пользователь вводит номер буквы в алфавите. Определить, какая это буква'''
alph_En = 'abcdefghijklmnopqrstuvwxyz'

num_of_char = raw_input('Введите номер буквы английского языка:')
if num_of_char.isdigit():
    num_of_char = int(num_of_char)
    if num_of_char > 0 and num_of_char <= 26:
        print('Буква под номером {} : {}'.format(num_of_char, alph_En[num_of_char - 1]))
    else:
        print('Вы ввели неверные данные')

else:
    print('Вы ввели неверные данные')
