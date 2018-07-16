# coding=utf-8
'''Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв'''
alph_En = 'abcdefghijklmnopqrstuvwxyz'
alph_Ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

char_one = raw_input('Введите первую букву: ').lower()
char_two = raw_input('Введите вторую букву: ').lower()
test_val = False

if char_one in alph_En and char_two in alph_En:
    alph = alph_En
    test_val = True

elif char_one in alph_Ru and char_two in alph_Ru:
    alph = alph_Ru
    test_val = True

elif (len(char_one) and len(char_two)) > 2:
    test_val = False

if test_val:
    print('Место буквы {}: {}'.format(char_one, alph.index(char_one) + 1))
    print('Место буквы {}: {}'.format(char_two, alph.index(char_two) + 1))
    count_char = abs(alph.index(char_two) - alph.index(char_one)) - 1
    print('Количество букв между ними: {}'.format(count_char))
else:
    print ('Вы ввели не верные данные')
