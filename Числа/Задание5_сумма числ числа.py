import random
print('\\' * 5, 'Начало', '\\' * 5)
    
#num = int(input('Введите число: '))
#num = int(num)
num = random.randrange(0, 999999)
num = str(num) # преобразуем int в str
num = list(num) # переобразуем строку в список
print('Число после приобразования:', num) # Печатаем список
print(type(num[0])) # Тип элементов массива
#num = [int(x) for x in num] # преобразуем элементы массива в int
#print(num) # Печатаем массив

# Преобразование массива в цикле
ints = []

for i in num:
    ints.append(int(i))
    
print(ints)
print(sum(ints)) # складываем элементы списка

# Преобразования списка через цикл
s = 0

for i in ints:
    s += i
    
print('s =', s)
    


c = random.randrange(0, 999999)
print(c)

clist = []
while c > 0:
    clist.append(c % 10)
    c //=10
print(clist)
    
# su_m = 0
# mult = 1
# # Вариант 1
# w c > 0:
#     digit = c % 10
#     su_m = su_m + digit
#     mult = mult * digit
#     print(su_m)
#     print(mult)
    