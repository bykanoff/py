def sumlist(n):
    n = str(n)
    n = list(n)
    n = [int(i) for i in n]
    return(sum(n))
        
    

num = input('Введите число: ')

if not num.isdigit():
    print('Введите число!')
elif len(num) < 2:
    print('Число должно быть больше 10!')
else:
    print(sumlist(num))
    
    