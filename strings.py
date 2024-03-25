"========String========"
# строки - неизменяевый тип данных, который проедназначен для хранения текста, заключенного в одинарные либо двойные ковычки

String1 = "строка с двойными кавычками"

String2 = 'c одинарными кавычками'

string3 = "dont't" # внутри двойных кавычек все одинарные кавычки - просто часть текста

string4 = 'Название магазина "Азбука"'

string5 = ''' 
Многострочный текст в 
одинврных кавычках 
тут можно использовать и одинарные и двойные 
кавычки
'''

string6 = """ 
Многострочный текст
в двойных кавычках
тут можно использовать и одинарные и двойные 
кавычки
"""

# string7 = "hello" + "world"
# print (string7)

# string8 = "A" * 20 # 20 раз буква А
# print(string8)



"========Экранизация строк========"

"\n" #перенос на новую строку

print ("hello world") # hello world

print ("hello\nworld")  # hello. 
                        #world

print ("he\nllo world") # sshe
                        # llo world



"\t" # табуляция (несколько пробелов)

# print ("hello\tworld") # hello   world

# print ("he\tllo world") # he   llo world


"\v" # перенос на новую строку со смещением вправо на длинну предыдущей строки

# print ("hello\vworld\vmakers") #hello
                                    #world
                                         #makers


"\r" # перенос каретки в самое начало строки

# print ("hello wold\rMa") # Mallo world


'\' ' # отображение '

"\" " # отображение "

# print ('don\'t') # don't

'\\' # это отображение \

# print ("команда \\n - переносит строку")



"=======Форматирование строк======="

# title = "IPhone 15"
# price = 1000
# # print("Я купил title за price $")
# shop = "Makers"

'1. f - строка'
# print (f"Я купил {title} за {price}$, в магазине {shop}")

'2. %s'
# print("Я купил %s за %s $ в магазине %s" % (title, price, shop))

'3. str.format'
# print ("Я купил {} pf {}$, в магазине {}".format(title, price, shop))


"=======Методы строк (str)======="

#  методы это функции, которые относятся к определенному типу данных (классу),  к ним мы относимся через точку

# print (dir(str))

string = 'hi'

print (string.upper()) # HELLO WORLD

print (string.lower()) # hello world

print (string.swapcase()) # hello WORLD # переводит буквы в противоположенный регистр (А>а)

print (string.title()) # Hello World

print (string.capitalize()) # Hello world

print (string. islower()) # true (маленькие буквы)

print (string. isupper()) # false (большиу буквы)

print (string.center(12, '*')) # '*****hi*****'

string = 'hello world'
print (string. count('l')) # 3
print (string. count('el')) # 1
print (string. count('o w')) # 1
print (string. count('hello')) # 1

print (string.startswith('h')) # true
print (string.startswith('H')) # false
print (string.startswith('hello')) # true
print (string.endswith('ld')) # true

string = 'makers'
print(string.isalpha()) # true, проверяет на буквы

print(string.isdigit()) # false, проверяет на числа

print(string.isalnum()) # true, проверяет на наличие букв и чисел (если есть символ то вернет false)

string = 'hello world maker bootcamp'
print (string.split()) # ['hello', 'world', 'makers', 'bootcamp'] (по умолчанию пробел, можно разделить по заданному символу)

print (string.replace('', '$')) #

string = ' hello ' 
print(string.strip( )) # убирает символы с начала и конца (так же можно убирать слева и справа по отдельности перед strip надо поставить l иил r)

# ''.join(string)  # list - это переменная которая хранит тип даннх list[]

"=======Индексы======="

# индекс - это пордковый номер элемента последовательности (индекс начинается с 0)

# -11-10-9-8-7-6-5-4-3-2-1
# 'h e l l o   w o r l d'
#  0 1 2 3 4 5 6 7 8 9 10

string = 'hello world'
print(string[0]) # h
print(string[-1]) # d
print(string[5]) # ' '

# срез [start:end:step]
string[6:10] # world
string[0:5] # hello
print(string[::2]) # hlowrd (перепрыгивает на указанное число)
print(string[::-1]) # dlrow olleh (зеркалит предложение в положительном значении)
print(string[::-2]) # drwolh

