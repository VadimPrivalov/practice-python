# Ввод трех чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Сортировка
sorted_numbers = sorted([a, b, c])

# Вывод
print("Числа в порядке возрастания:", sorted_numbers)


def calculate_salary(sales):
    base = 200
    if sales < 500:
        return base + sales * 0.03
    elif 500 <= sales < 1000:
        return base + sales * 0.05
    else:
        return base + sales * 0.08

# Ввод продаж для трех менеджеров
sales1 = float(input("Введите продажи первого менеджера: "))
sales2 = float(input("Введите продажи второго менеджера: "))
sales3 = float(input("Введите продажи третьего менеджера: "))

# Расчет зарплат
salary1 = calculate_salary(sales1)
salary2 = calculate_salary(sales2)
salary3 = calculate_salary(sales3)

# Определение лучшего менеджера
max_sales = max(sales1, sales2, sales3)
if max_sales == sales1:
    salary1 += 200
    best = "Первый менеджер"
elif max_sales == sales2:
    salary2 += 200
    best = "Второй менеджер"
else:
    salary3 += 200
    best = "Третий менеджер"

# Вывод результатов
print(f"Зарплата первого менеджера: {salary1:.2f}$")
print(f"Зарплата второго менеджера: {salary2:.2f}$")
print(f"Зарплата третьего менеджера: {salary3:.2f}$")
print(f"Лучший менеджер: {best} (премия 200$)")



import calendar

year = int(input("Введите год: "))
month = int(input("Введите месяц (1-12): "))

# Проверка ввода
if month < 1 or month > 12:
    print("Ошибка: месяц должен быть от 1 до 12!")
else:
    days = calendar.monthrange(year, month)[1]
    print(f"В {month}-м месяце {year} года {days} дней.")

    age = int(input("Введите возраст посетителя: "))
    time = int(input("Введите время сеанса (часы, например 14): "))

    # Определение базовой цены
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    # Применение скидки (20% до 12:00)
    if time <= 12 and price > 0:
        price *= 0.8

    print(f"Стоимость билета: {price:.2f}$")