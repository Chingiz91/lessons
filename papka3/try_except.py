




NameError
#исключение, которое выходит, когда мы обращаемся к несуществующей переменной


'''
num 1 = 15
print(num15)
NameError
'''


IndexError
# исключение, которое выходит, когда мы обращаемся по несуществующему индексу

'''
list_ = [12, 20, 0, 2].pop()
IndexError
'''

'''
[12, 0, 24, 'hi'].pop(1000)
IndexError: pop from empty list
'''

KeyError
# исключение, которое выходит, когда мы обращааемся по не существующему ключу

'''
dict_ = {'a': 1}
dict_['c']
KeyError
'''


'''
dict_{'a': 1}
dict_.get('c')
ошибки не будет!!! Так как get не вызывает ошибку, а вкрнет None, если такого ключа нет
'''

ValueError
# ислючение, которое выходит когда мы передаем в функцию не корректный для нее тип дпнных
# исключение, которое выходиткогда мы распаковываем интерируемый объект на несколько переменных и количество переменных не совпадает с количеством элементов

'''
int('10dfh')
ValueError
'''

'''
a, b, c = 2, 3
ValueError
'''


TypeError
# исключение, которое выходит, когда мы пытаемся использовать методы не свойственные какому-то типу данных
# когда мы пытаемся передать функции больше или меньше аргументов, чем принимает функция 

'''
for i in 1234:
...
TypeError
'''

'''
'5' + 5
TypeError
'''

'''
{[1,2,3]: 'hi'}
TypeError
'''

'''
input('Ввведите число', 123)
TypeError
'''

'''
[].append()
TypeError
'''

ZeroDivisionError

# возникает тогда, когда мы собираемся делить на 0

'''
45 / 0
ZeroDivisionError
'''

'''
45 // 0
ZeroDivisionError
'''

'''
45 % 0
ZeroDivisionError
'''

AttributeError

# выходит, когда мы обращаемся к несуществующему аттребуту или методу обьекта (типа данных)

'''
[1, 23, 1, 56].replace('a', ' ')
AttributeError
'''

'''
'makers'.pop(0)
AttributeError
'''


IndentationError

# выходит, когда мы неправильно используем отстпупы

'''
a = 5
IndentationError
'''

'''
for i in range(11)
print(i)
IndentationError
'''


Exception

# исключение, которое создали, что бы его вызывать


'=============Вызов исключений============'

# принкдительный вызов производится при поиощи RAISE

# raise NameError ('Просто вызываю NameError')
# raise IndexError
# raise KeyError


'============Обратотка исключений============'

# нужна что бы код не прекращал свою работу, мы можем использовать конструкцию try-except и обрабатывать вызванное исключение



# try:  # код который может вызвать ошибку/исключение
#     num = int (input ('Введите число: '))
# except ValueError: # пишем ожидаемое исключение
#                    # Обработку на исключение, которое поймали
#     print('Вы ввели не число')
# else:   # код, который отработает, усли исключения (ошибки) не вышло
#     print(f'Вы ввели число {num}')
# finally:  # Работает всегда
#     print ('До свидания')


# try:
#     num = int (input ('Введите число: '))
#     res = 10 / num
#     print(num)
# except (ValueError, ZeroDivisionError, NameError):
#     print ('Что-то пошло не так')



# try:
#     num = int (input ('Введите число: '))
#     res = 10 / num
# except ValueError, ZeroDivisionError:
#     print ('Что-то пошло не так')
# except ZeroDivisionError:
#     print('Введите число кроие 0')


# except Exception: - обрабатывает все исключения, которые могут выйти
# except: обрабатывает все исключения, которые могут выйти
    

# можем указать в except несколько исключений при помощи скобок и запятой except (ValueError, ZeroDivisionError, NameError)
    

# try:
#     raise NameError
# except NameError:
#     print(1)


try:
    num = input('Введите число: ')
    if num == 0:
        raise ZeroDivisionError
    elif num > 0:
        raise ValueError
    elif num < o:
        raise TypeError
except ValueError:
    print('положительное')
except TypeError:
    print('отрицательное')
except ZeroDivisionError:
    print('0')