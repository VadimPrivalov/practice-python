def check_interval(number):
  """
  Проверяет, принадлежит ли число интервалу (-9; 2).
  Интервал строгий, то есть -9 и 2 не включаются.
  """
  if -9 < number < 2:
    return f"Число {number} принадлежит интервалу (-9; 2)."
  else:
    return f"Число {number} НЕ принадлежит интервалу (-9; 2)."

# Запрашиваем у пользователя ввод числа
try:
  user_input_str = input("Введите число: ")
  user_number = float(user_input_str)
  result = check_interval(user_number)
  print(result)
except ValueError:
  print("Ошибка: введите корректное число.")