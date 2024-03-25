'=========Set========'
# множества - изеняемый, неупорядоченный, итерируемый тип данных, предназначенный для хранения уникальных значений. Множества могут хранить в себе только неизменяемый тип данных. Если внутри set, используется tuple, то и внутри tupl'a должны быть неизменяемые типы данных ({1,2,3,0,23,('str', 12, True)}). В set работает правило - FIFO (first in first out)


# set_1 = {1, 0, True, 'hi'} # не могут использоваться одинаковые значения, при использовании одинаковых значений последнее значение удаляетсяю
# print(set_1)


'==========FIFO/LIFO=========='
# FIFO - first in first out (оередь в банк, выйдет первым тот, кто первым стал в очередь)
# LIFO - last in first out  (выйдет та бумага, которую вы поставили последней)


'==========Методы set=========='
'add - добавляет элементы в set'

# set1 = {1,2,3}
# set1.add(3) # {1,2,3} ничего не изменится
# set1.add(1,2,3,4,5) # {1,2,3,4,5}
# print(set_1) # {1,2,3,4,5}


'pop - удаляет случайный элемент из set'

# set2 = {1,2,3}
# popped = set2.pop()
# print(set2)


'remove - удаляет элемент из set по значению'

# set3 = {1,2,3}
# set3.remove(3)
# print(set3)


# print(dir(set))


'union - обьеденяет set1 и set2'

# set1  = {1,2,3}
# set2 = {4,5,6}
# print(set1.union(set2))
# print(set1)


'update - обьеденяет set1 и set2 и сохраняет изменение в set1'

# set1  = {1,2,3}
# set2 = {4,5,6}
# set1.update(set2)
# print(set1)


'diference (-) находит разницу из set1 при помощи set2'

# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.difference(set2)) # {1,2}
# print(set2.difference(set1)) # {4,5}
# print(set1 - set2) #с= сокращенный способ differce знак (-)
# print(set2 - set1) #с= сокращенный способ differce знак (-)


'simmetric_difference - находит разницу из двух сетов'

# set1 = {1,2,3}
# set2 = {3,4,5}
# print (set1.symmetric_difference(set2)) # {1,2,4,5}



'intesection (&) - находит схожие элементы из двух сетов set1, set2'

# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# print (set1.intersection(set2)) # {3,4}
# print (set1 & set2) # {3,4}

# print(dir(set)) !!!!!!!
