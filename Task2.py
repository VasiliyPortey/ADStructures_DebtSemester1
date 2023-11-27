from random import randint

list_length = int(input('Введите длину массива: '))
numbers_list = []
sum = 0
for i in range(list_length):
    numbers_list.append(randint(-10, 10))

print('Исходный массив:\n', numbers_list)
    
for i in range(list_length):
    sum += numbers_list[i]
    
avrg_value = float(sum)/list_length
print('Среднее арифметическое чисел в массиве = ', avrg_value)