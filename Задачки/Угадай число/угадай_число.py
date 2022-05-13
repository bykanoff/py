# импортируем модуль для генерации случайных чисел
import random

num = random.randrange(1, 100)

while True:
    answer = input('Введите число: ')
    # проверяем, что введенное значение число
    if not answer.isdigit():
        print('Надо ввести число!')
        continue
    
# если введенное значение является числом
# выполняем следующий код

    answer = int(answer)
    if answer > num:
        print('Меньше')
    elif answer < num:
         print('Больше')
    else:
        print('Правильно')
        break # значение верно цикл прирывается