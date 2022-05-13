# Задача на остаток от деления:

print('*' * 5, 'Остаток после деления', '*' * 5,'\n')

while True:
    stud = input('Введите количество студентов: \n')
    apples = input('Введите количество яблок: \n')
    
    if not stud.isdigit() and apples.isdigit:
        print('Требуется ввести число!')
        continue
    else:
        stud = int(stud)
        apples = int(apples)
        print(f'У студентов {apples // stud} яблок\nВ корзине {apples % stud} яблок\n') 
        break
print('*' * 5, 'Конец', '*' * 5)
