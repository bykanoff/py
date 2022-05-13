# Функция по вычислению площади круга
# Сама функция
def area_of_disk(radius):
    return 3.14 * radius ** 2
r = area_of_disk(3)
print(r)

# Вычисление площади диска
# Пишем еще одну функцию
def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)
outer = input('Введите радиус внешнего круга: ')
inner = input('Введите радиус внутреннего круга: ')
outer = int(outer)
inner = int(inner)
r_1 = area_of_ring(outer, inner)
print(r_1)

