#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


# N = (input('Введите число: '))

# str_N = str(N)
# str_N = str_N.replace(',', '')
# str_N = str_N.replace('.', '')
# list_str = list(str_N)
# lst_num = map(int, list_str)
# a = sum(lst_num)
# print(a)




#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)



# N = int(input('Введите число '))

# f = 1
# for i in range(N):
#     i = i + 1
#     f = i * f
    
#     print(f, end=" ")



#3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# n = int(input('Введите число: '))   
# d = {}

# for i in range(1, n+1):
#     d[i] = 3*i+1

# print(d)




#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

from random import Random, randint

n = int(input('Введите число '))
numbers = []
for i in range(-n, n+1):
    numbers.append(randint(-n,n+1))
print(numbers)

f = open('file.txt', 'w')
while True:
    s = input('Укажите позицию для вычисления - ')
    if s == "":
        break
    f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)