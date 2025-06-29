#Задача 1: Простой калькулятор
#Напишите программу, которая запрашивает у пользователя два числа и оператор (+, -, *, /), а затем выполняет соответствующую операцию и выводит результат.

num1 = float(input("Введите первое число: "))
operator = input("Введите оператор (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль!"
else:
    result = "Ошибка: неверный оператор!"

print(f"Результат: {result}")

# Задача 2: Поиск простых чисел в заданном диапазоне
# Напишите программу, которая запрашивает у пользователя начало и конец диапазона и выводит все простые числа в этом диапазоне.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start > end:
    print("Ошибка: начало диапазона должно быть меньше конца!")
else:
    print(f"Простые числа в диапазоне от {start} до {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')