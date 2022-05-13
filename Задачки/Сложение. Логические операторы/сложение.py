# # Импортируем модуль random
# # random генерирует случайные числа
# import random
# # указываем диапазон генерации чисел
# n1 = random.randrange(1, 11) # если указать одно генерация будет от нуля до минус 1 от указанного
# n2 = random.randrange(1, 101)
# 
# answer = input(f'Сколько будет {n1} + {n2}?: ')
# # подключаем метод replace, заменяем точку в ответе 1раз
# test = answer.replace('.', '', 1)
# # тестируем переменную test
# if not test.isdigit():
#     print('Надо ввести число!)
# # условие проверяющее ввод данных
# # поле принимает только числа
# if answer.isdigit(): # проверяем что введенное значение число
#     if answer == n1 + n2:
#         print('Правильно')
#     else:
#         print('Неправильно')
# else:
#     print('Надо ввести число!')
#     

# финальная версия программы
# подключаем модуль random
import random
# определяем диапазон сгенерированных чисел
n1 = random.randrange(1, 11)
n2 = random.randrange(1, 111)
# предлагаем пользователю указать сумму
answer = input(f'Сколько будет {n1} + {n2}?: ')
# заменяем точку в ответе пользователя, если число float
test = answer.replace('.', '', 1)
# проверяем евляется ли числом переменная test
if not test.isdigit():
    print('Надо ввести число!')
# проверяем равен ли answer переменной test
# для того что бы понять целое число было введено или нет
else:
    if answer == test:
        answer = int(answer)
    else:
        answer = float(answer)
    if answer == n1 + n2:
        print('Правильно')
    else:
        print('Неправильно')
        

