'==========Циклы========='
# цикл - это конструкция, которая повторяет код несколько раз
# в питоне имеется 2 вида цикла

'1. for - цикл, который работает с интерируемым объектом. Цикл заканчивает работу, когда доходит до последнего элемента интерируемого объекта'

'2. while - цикл, который, работает до тех пор пока условие верное (True)'

'Интерируемый объект - это последоватклтность (откуда мы можем доставать элементы), например: [1, 23, "hi"], "makers", (123, True, 1, 5), dict, set'

'Итерация - процесс перебора итерируемого объекта (когда мы поочереди вытаскиваем элементы в последовательности)'

'--------------------------'

'FOR'

# list_ = [12, 'hi', True, None, [0, 0, 0]]
# for i in list_:
#     print(i)

'--------------------------'

# for letter in 'hello world':
#     print(letter)

#h
#e
#l
#l
#o
# 
#w
#o
#r
#l
#d


'--------------------------'

# for number in [12, 3, 4, 0, -1, 20]:
#     print(number * 2)
    
# # 24
# # 6
# # 8
# # 0
# # -2
# # 40
    
# list_ = [2, 12, 5, 3]
# for i in list_:
#     print(i ** 2) # во второй спепени


'------------------------'

# text = 'makers'
# for i in text:
#     print(i)


# '-------------------------'


# list_ = [2, 5, 20, 10, 9, -1]
# for i in list_:
#     if i % 2 == 0: # формула для выдачи только чеиных чисел
#         print(i) 
   


'WHILE'

# n = 1
# while n < 10:
#     print ('hello world')
#     n = n + 1


# n = 0
# while n < 10:
#     print('hi')
#     n += 1


               #останавливает код в терминале
                   # ctrl + c либо ctrl + z
 

'============Ключевые слова в циклах============'

# break - принудительная остановка цикла
# cintinue -  пропускает итерацию, продолжает со следующей итерации

# range ()  # генератор

# for i in range(1, 11):
#     if i == 3:
#         continue
#     print(i)

#1
#2
#4
#5
#6
#7
#8
#9
#10
    


# for i in range(11):
#     print (i)
#     if i == 2:
#         break

#0
#1
#2

# n = 1
# while n < 10:
#     n = n + 1
#     if n == 2:
#         continue
#     print(n)

#3
#4
#...
#9
    

n = 0
while n < 10:
    print(n)
    if n > 5:
        break
    n += 1  # n = n + 1 (один и тот же код) 