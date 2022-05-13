# Расчет секунд и минут

while True:
    print('-' * 5, 'Начало', '-' * 5,'\n')
    N = input('Введите количество секунд: \n')
    if not N.isdigit():
        print('Введите целое число секунд!')
        continue
    else:
        N = int(N)
        hour = (N // 3600)
        minets = (N % 3600)//60
        if hour > 23:
            print(f'После полунучи прошло {hour // 23} часов, {minets} минут(-ы).\n')
        else:
            print(f'После полуночи это: {hour} часов, минут(-ы): {minets}\n')
            
    print('-' * 5, 'The End', '-' * 5)
    break   
