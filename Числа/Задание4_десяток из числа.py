import random
print(f'***** Начало *****')
def dozer(n):
    return (str(n)[-2])
while True:
    num = random.randrange(0, 999)
    if num > 9: 
        print(num)
        print(dozer(num))
        continue
    else:
        print(num)
        print('В числе нет десятков!')
        break
    
            
