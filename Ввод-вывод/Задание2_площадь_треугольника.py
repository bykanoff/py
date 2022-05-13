# Расчет площади прямоугольного треугольника
while True:
    print("*" * 5, "Расчет площади прямоугольного треугольника", "*" * 5, "\n")
    while True:
        a = input("Введите длину основания треугольника: \n")
        if not a.isdigit():
            print("-" * 5, "Please, enter the number!", "-" * 5, "\n")
            continue
        else:
            break
    while True:
        b = input("Введите длину высоты треугольника: \n")
        if not b.isdigit():
            print("-" * 5, "Please, enter the number: ", "-" * 5, "\n")
            continue
        else:
            break
    
    a = int(a)
    b = int(b)
    
    S = 0.5 * a * b
    print("!" * 3, "Площадь треугольника равна: ", S, "!" * 3, "\n")
    break

