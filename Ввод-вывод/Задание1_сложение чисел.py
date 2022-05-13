# Домашняя работа сумма 3 чисел
while True:
    print("*" * 5, "Сумма чисел", "*" * 5)
    #Ввод чисел
    while True:
        a = input("Enter the first number: \n")
        if not a.isdigit():
            print("Enter number!")
            continue
        else:
            break
    while True:
        b = input("Enter the second number: \n")
        if not b.isdigit():
            print("Enter number!")
            continue
        else:
            break
    while True:
        c = input("Enter the third number: \n")
        if not c.isdigit():
            print("Enter number!")
            continue
        else:
            break
        
    a = int(a)
    b = int(b)
    c = int(c)
    
    
    sum = a + b + c
    print("Результат вычисления равен:", sum)
    break

