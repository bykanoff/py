print('\'' * 5, 'START', '\'' * 5)

with open('fish_text.txt', encoding='utf-8') as s:
    #words = s.split('.')
    f = s.read()
    words = f.split('.')
    for i in words:
        print(i,'.', sep='') #уберает пробелы между переменными
    
    
    
#     with open('fish_text_out.txt', 'a', encoding='utf-8') as out:
#         for line in filter(lambda x: x == '.', s):
#             out.write(line)

print('\\' * 5, 'FINISH', '\\' * 5)