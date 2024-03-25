'===========Словари=========='

#dict - изменяемый, итерируемый, неупорядоченный (псевдопорядок), неиндексируемый тип данных, для хранения данных в парах {ключ: значение}

# users = {'name': 'Anonym', 'age': 30, 'last_name': 'Makers'}
# print(users['name']) #Anonym
# print(users['age']) # 30
# print(users['last_name']) # Makers

# ключами в словаре могут быть только неизменяемые типы данных
# ключи в словорях должны быть уникальными

'===========Создание словарей=========='

# dict_ = {'a': 1, 'b': 2}
# dict_ = dict([('a',1),('b',2)])
# print(dict_)
# dict_ = dict(['a1', 'b2', 'c3'])
# print(dict_)      # {'a':'1', 'b':'2', 'c': '3'}

# dict_= {}
# dict_['name'] = 'makers'
# dict_['age'] = 50
# dict_['last_name'] = 'bootcamp'
# print(dict_)


'==========Методы словаря========='

'get - метод, который плучаеет значение по ключчу, если указанного ключа нет, то выходит None - по умолчанию, мы можем его поменять'

# user = {
#     'name': 'Anonym', 
#     'age': '15', 
#     'last_name': 'Makers'
    # }
# print(user['id']) # error - KeyError
# print(user.get('id')) # None
# print(user.get('name', 'Такого ключа нет')) # Такого ключа нет


'pop - удаляет пару по ключу и возращает значение'

# dict_ = {'a':1, 'b':2, 'c': 3}
# popped = dict_.pop ('b')
# print(dict_) # {'a':1, 'c':3}
# print(popped) # 2


'popitem - удаляет последнюю пару и возвращает ее'

# dict_ = {'a':1, 'b':2, 'c':3}
# popped = dict_.popitem()
# print(dict_) #{'a':1, 'b':2}
# print(popped) # ('c', 3)


'update - расширяет словарь парами из второго словоря'

# dict_1 = {1:'a', 2:'a'}
# dict_2 = {2:'b', 3:'b'}
# dict_1.update(dict_2)
# print(dict_1) # {1:'a', 2:'b', 3:'b'}


'clear - очищает словарь'

# dict_1 = {'a':1, 'b':2, 'c':3}
# dict_1.clear()
# print(dict_1) # {}


'fromkeys - метод для создания нового словоря, используя список ключей'

# dict_ = dict.fromkeys('hi')
# print(dict_) # {'h':None, 'i':None}
# dict_2 = dict.fromkeys(['hi', 123, True], 0)
# print(dict_2) #{'hi':0, 123:0, True:0}


'keys, values, items'
# keys - метод, который возвращает все ключи
# values - метод, который возвращает все значения
# items - метод, который возвращает пары: ключ и значение в виде tuple

user = {
    'name': 'Anonym',
    'age': 15,
    'last_name': 'Makers'
}
print(user.keys()) #dict_keys(['name', 'age', 'last_name'])
print(user.values()) #dict_values(['Anonym', 15, 'Makers'])
print(user.items()) #dict_items([('name', 'Anonym'), ('age', 15), ('last_name', 'Makers')])

'============Итерирование словарей============'

# user = {
#     'name': 'Anonym',
#     'age': 15,
#     'last_name': 'Makers'
# }
# for key in user: 
#     print(key)
# # при итерации словоря с методом key, будут приходить ключи

# for value in user.values():
#     print(value)
# # при итерации словоря с методом values, приходят значения

# for item in user.items(): 
#     print(item)
# # при итерации словоря с методом items, приходят tuple с ключем и значением
    
'---------------------------------'

# dict_1 = {
#     1:'a',
#     2:'b'
# }
# dict_2 = {}
# for k, v in dict_1.items():
#     dict_2 [v] = k
# print(dict_2)