#1. Напишите программу, которая принимает строку от пользователя и выводит ее в обратном порядке.
#s = input("Введите строку: ")
#print(s[::-1])
from itertools import permutations

#2. Напишите программу, которая принимает две строки и проверяет, являются ли они анаграммами (то есть состоят из одних и тех же символов в любом порядке).
#s1 = input("Введите строку: ").lower()
#s2 = input("Введите строку: ").lower()
#print(sorted(s1) == sorted(s2))

#3. Напишите программу, которая принимает строку и подсчитывает количество гласных и согласных букв в ней.
#s = input("Введите строку: ").lower()
#vowels = "ФВФЫВЫЬВЬЫВУЕее"
#consonants = "ТОТЫВЫГШВОТЫФ"
#v = c = 0
#for char in s:
#v += 1
#elif char in consonants:
#c += 1
#print("Главных:", v)
#print("Согласных:", c)

#4. Напишите программу, которая принимает строку и проверяет, является ли она палиндромом (то есть одинаково читается в обоих направлениях).
 #s = input("Введите строку: ").lower().replace(" ", "")
#if s == s[::-1]:
 #    print("Палиндром")
 #else:
  #   print("Строка не является  палиндромом")
#*5. Напишите программу, которая принимает строку и выводит на экран все перестановки ее символов.
# s = input("Введите строку: ")
# a = list(s)
# n = len(a)
# index = 0
# stack = [(a, 0)]
#
# while index < len(stack):
#     current, l = stack[index]
#     index += 1
#
#     if l == n - 1:
#         print("".join(current))
#     else:
#         i = n - 1
#         while i >= l:
#             temp = current[:]
#             temp[l], temp[1] = temp[i], temp[l]
#             stack.append((temp, l + 1))
#             i -= 1
# Решение через импорт permutations
# s = input("Введите строку: ")
#perms = permutations(s)
#for p in perms:
#   print("".join(p))


#напишите процедуру которая принимает праметр -
# натуральное число N - и выводит на экран две линии из N символов "-".
#def print_lines(n):
#   print("-" * n)
#   print("-" * n)
#n = int (input("Введите кол-во символовв в строке: ")
#print(print_lines(n))

#напишите процедуру,которая принимает один параметр - натурльное число N, - и выводит на экран прямоугольник длиной N высотой 3 символа.

#def print_rectangle(n):
#   if n < 2:
#      print("Ширина должна быть не менее 2-x")
# print("-" * n)
#  print("#" + " " * (n - 2) +"#")
#  print("-" * n)
#n = int(input("Введите ширину прямоугольника: "))
#print_rectangle(n)


#Напишите процедуру которая выводит  на экран треуголник со стороной N символов. При запуске программы N нужно вести с клавиатуры
#def print_triangle():
#    N = int(input("Введите размер треугольника: "))
    #    for i in range(1, N + 1):
#       print('*' * i)

#print_triangle()


#напишите функцию которая вычисляет среднее арифмитическое пяти целых чисел
#def calculate_average():
#  numbers = []
# print("Введите 5 целых чисел:")

# for i in range(5):
#    while True:
            #       try:
#        num = int(input(f"Число {i + 1}: "))
#        numbers.append(num)
#        break
        #    except ValueError:
#        print("Ошибка! Введите целое число.")

#  average = sum(numbers) / len(numbers)
# print(f"Среднее арифметическое: {average}")
# return average


# Пример вызова функции
#calculate_average()

