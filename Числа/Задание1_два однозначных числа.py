# Числа требуется из двузначного сделать два однозначных целых
print('*' * 5, 'Начало', '*' * 5)
while True:
    num = input("Введите целое двузначное число: ")
    if not num.isdigit() and len(num) < len(2):
        print("Введите целое двузначное число!")
        continue
    else:
        num = int(num)
        print(num % 10, num // 10)
        continue
    
        
        
        

        

    