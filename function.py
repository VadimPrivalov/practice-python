#Найти все трехзначные простые
#числа:
#(Определить функию,позволяющую распознать простые числа.)

# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#         return True
#
# primes = []
# for i in range (100, 1000):
#     if is_prime(i):
#         primes.append(i)
# print(primes)





# Задача 7
# Найти периметр треугольника, заданного координатами своих вершин.
#(Определить функцию для расчета длины отрезка по координатам его вершин.)
# def distance(x1, y1, x2, y2):
#     return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
#
# def triangle_perimetr(x1, y1, x2, y2, x3, y3):
#     a = distance(x1, y1, x2, y2)
#     b = distance(x2, y2, x3, y3)
#     c = distance(x3, y3, x1, y1)
#     return a + b + c
#
# print(triangle_perimetr(1,  2,  4,  5,  6,  7))



# Задача 9
#Получить все шестизначные счастливые номера.Счастливым номером назыввают такое шестизначное число,
#в котором сумма его первых трец цифр равна сумме его последних трех цифр:
#(Определить функцию для расчетаа суммы цифр трехзначного числа.)
# def sum_digits(n):
#     summa = 0
#     for d in str(n):
#         summa += int(d)
#     return  summa
#
#
# def is_lucky(n):
#     s = str(n)
#     if sum_digits(s[:3]) == sum_digits(s[3:]):
#         print("Число счастливое")
#     else:
#         print("Число не счастливое")
#
# is_lucky(11101)



#Задача 10.
#Даны шесть разных чисел.Определить максимальное из них.
#(Определить функцию,находящую максимум из даух различных чисел.)


def max6(a, b, c, d, e, f):
    return max(a, b, c, d, e, f)

print(max6(2, 3, 4, 5, 5,3,))