# Расчет времени разницы секунд между двумя временными метками

print('-' * 5, 'Вычисляем разницу секунд между двумя метками времени', '-' * 5, '\n')
print('*' * 5, 'Введите временные интервалы', '*' * 5, '\n')
while True:
    print('Введите первое показание: \n')
    while True:
        h = input('Часы: ')
        if not h.isdigit():
            print('Введите число!')
            continue
        h = int(h)
        if h > 23:
            print('В cутках 23 часа 59 минут!!!')
            continue
        else:
            break
    while True:
        m = input('Минуты: ')
        if not m.isdigit():
            print('Введите число!')
            continue
        m = int(m)
        if m > 60:
            print('В часе 60 минут!!!')
            continue
        else:
            break
    while True:
        s = input('Секунды: ')
        if not s.isdigit():
            print('Введите число!')
            continue
        s = int(s)
        if s > 60:
            print('В минуте 60 секунд!!!')
            continue
        else:
            break
    print('\n')  
    print('Введите второе показание: \n')
    
    while True:
        h1 = input('Часы: ')
        if not h1.isdigit():
            print('Введите число!')
            continue
        h1 = int(h1)
        if h1 > 23:
            print('В сутках 23 часа 59 минут!!!')
        else:
            break
    while True:
        m1 = input('Минуты: ')
        if not m1.isdigit():
            print('Введите число!')
            continue
        m1 = int(m1)
        if m1 > 60:
            print('В часе 60 минут!!!')
            continue
        else:
            break
    while True:
        s1 = input('Cекунды: ')
        if not s1.isdigit():
            print('Введите число!')
            continue
        s1 = int(s1)
        if s1 > 60:
            print('В минуте 60 секунд!!!')
            continue
        else:
            break

    difSec = int((h * 3600) + (m * 60) + s)
    difSec1 = int((h1 * 3600) + (m * 60) + s)
    while True:
        if difSec > difSec1:
            print(difSec - difSec1)
            break
        else:
            print(difSec1 - difSec)
            break
    break
    

