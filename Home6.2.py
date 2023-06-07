# 6.2[32]: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

# (*) Усложнение. Функция возвращает список кортежей вида: индекс, значение

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]

def Show_me_the_numbers_and_indexes(list1:list, min_num: int, max_num: int) ->list:
    result_list=[]
    for index in range(len(list1)):
        if list1[index]>=min_num and list1[index]<=max_num:
            my_tuple = (index, list1[index])
            result_list.append(my_tuple)
    return result_list

def Show_me_the_indexes_only(list1:list, min_num: int, max_num: int) ->list:
    result_list=[]
    for index in range(len(list1)):
        if list1[index]>=min_num and list1[index]<=max_num:
            result_list.append(index)
    return result_list

lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print('lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]')
print('Show_me_the_numbers_only(lst1, 2, 10):')
print(Show_me_the_indexes_only(lst1, 2, 10))

print('Show_me_the_numbers_only(lst1, 2, 9):')
print(Show_me_the_indexes_only(lst1, 2, 9))

print('Show_me_the_numbers_only(lst1, 0, 6):')
print(Show_me_the_indexes_only(lst1, 0, 6))

print('Show_me_the_numbers_and_indexes(lst1, 2, 10):')
print(Show_me_the_numbers_and_indexes(lst1,2,10))