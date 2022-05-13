print('*' * 5, 'Меняем цифры местами', '*' * 5)

num = input('Введите двузначное целое число: \n')
#num = int(num)
while True:
    if not num.isdigit() or (len(num) < 2 or len(num) > 2):
        print('Введите целое двузначное число!')
        continue
    else:
        print(str(num)[::-1])        
        break

#Функция:
def fun(number):
    return str(number)[::-1]
    
 
print(fun(num))
