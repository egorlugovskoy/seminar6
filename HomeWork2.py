# Задача 2.Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform

size = int(input('Введите размер списка '))
my_list = []
for i in range(size):
     i = uniform(0, 10)
     my_list.append(round(i, 2))
print(my_list)
new_list = []
l = list(map(lambda i: round(i%1, 2), my_list))
new_list = l
print(new_list)
min = new_list[0]
max = 0
for i in range(len(new_list)):
         if max < new_list[i]:
             max = new_list[i]
         if min > new_list[i]:
              min = new_list[i]
dif = max - min
print(f'max = {max}, min = {min}')
print(f'Разница между max и min = {(round(dif, 2))}')