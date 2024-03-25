'===========Comprehensions============'
# генератор, с помощью которого можно создать последовательность используя цикл for в одну строку

# range ()
# []
# {}
# {:}

# результат for элемент in  последовательность

# list_1 = [x + 2 for x in range (11)]
# print(list_1) # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# list_ = []
# for i in range(1,11):
#     if i % 2 == 0:
#         list_.append(i)
# print(list_)

# list_ = [i if i % 2 == 0 else i*2 for i in range (1,11)]

'в comprehension  можно добавлять условияб там их бывает 2 вида'

'1  - тернарный оператор, пишется перед цикло, так как используется и if и else'
'2 - фильтр, пишется после цикла,, так как используется только if'



# list_1 = [12, True, None, 'hi', 0, False, 'makers', 'world']

# list_1 = [ i for i in list_1 if type(i) == str]
# print (list_1)


'============Виды comperhension==========='

'1 - list comperhension'
'2 - dict comperhension'
'3 - set comperhension'


'Dict comperhension'

# dict_1 = {i:i ** 2 for i in range (1,11)}
# print(dict_1)
# # {1:1, 2:4, 3:9, ...}


# dict_1 = {'a':1, 'b':2, 'c':3}
# dict_2 = {value: key for key, value in dict_1.items()} #{1:'a', 2:'b', 3: 'c'}
# print(dict_2)


# dict_1 = {
#     'a':[1,2,3],
#     'b':[12,0,1],
#     'c':[32,0,0,10]
# }

# dict_2 = {k:sum(v) for k, v in dict_1.items()} 
# print(dict_2)
# # {'a': 6, 'b': 13, 'c': 42}

'Set comperhension'

# set_1 = {i for i in range (1,11)}
# print (set_1)
# # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# set_2 = {i for i in 'makers'}
# print (set_2)
# # {'s', 'm', 'e', 'r', 'a', 'k'}


# set_1 = {2, 3, 4, 15, 1}
# set_2 = {i**2 for i in set_1} # !!!!!!!! где i переменная в которой хранятся данные !!!!!!!!!
# print (set_2)

# set_1 = {2, 3, 4, 15, 1}
# set_2 = {i**i for i in set_1} # {256, 1, 4, 437893890380859375, 27}
# print (set_2)


# set_1 = {12, 4, 34, 5, 6}
# set_2 = {str(i) for i in set_1} # {'5', '6', '34', '12', '4'} перевели числа в строки
# print(set_2)


# set_1 = {1, 12, 'hi', 34, True, 'makers'}
# set_2 = {i for i in set_1 if type(i) == str} # {'hi', 'makers'}
# print(set_2)


# set_1 = {12, True, 'HI', 23, '10', 'makers', False, '1'}
# set_2 = {int(i) if i.isdigit() else i for i in set_1 if type(i)==str}
# print(set_2) #{'makers', 1, 10, 'HI'}


# dict_1 = {i:[i for i in range (1,i+1)] for i in range(1,6)}
# print(dict_1) # {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}