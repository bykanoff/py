# Программа, которая печатает на 1 меньше и на 1 больше
print('*' * 5, 'Numbers, more and less', '*' * 5,'\n')

while True:
    a = input("Введите любое число, для выхода нажмите Q: \n")
    if a == 'q' or a == 'Q':
        print('-' * 5, 'Cпасибо за внимание!!!', '-' * 5)
        break
    elif not a.isdigit():
        print(f'Это не похоже на число!!!\n')
        continue
    else:
        a = int(a)
        print(f'Следующее число для числа {a}: {a + 1}\nСледующее число для числа {a}: {a - 1}\n')