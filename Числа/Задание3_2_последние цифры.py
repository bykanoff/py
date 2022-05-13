import random # Импортируем модуль рэндом для случайной генерации чисел
def lastnum(number):
    return str(number)[-2:]

print('*' * 5, 'Начало', '*' * 5)
while True:
    num = random.randrange(0, 999)
    num = str(num)
    if len(num) < 2:
        print(num)
        print('Число должно быть двузначным!')
        break
    else:
        print(num)
        print(lastnum(num))
        continue
        
        

