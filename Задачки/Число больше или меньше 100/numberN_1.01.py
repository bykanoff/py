# Программа, число больше или меньше 100:
while True:
    n = input('Введите число: ')
    #n = int(n) # если определить переменную здесь инструкция .isdigit не сработает
    if not n.isdigit():
        print('*' * 5,'Please, enter number', '*' * 5)
    elif n.isdigit():
        n = int(n)
        if n < 100:
            print("*" * 5, "Введенное число меньше 100", "*" * 5)
        elif n > 100:
            print("*" * 5, "Введенное число больше 100", "*" * 5)
        else:
            print("*" * 5, "Число равно 100", "*" * 5)
            break