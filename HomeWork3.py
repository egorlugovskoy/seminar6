# Задача 3.

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
size = int(input('Введите размер списка: '))
my_list = []
for i in range(size):
     my_list.append(random.randint(0, 10))
print(my_list)
list = [my_list[index] for index in range(1, len(my_list) + 1, 2)]
print(f'Сумма чисел с нечетными индексами равна = {sum(list)}')