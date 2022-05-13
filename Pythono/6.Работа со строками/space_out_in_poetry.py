print('\'' * 5, 'START', '\'' * 5)

#a = input('Вставьте стихотворение из файла: ')

# удаляем пустые строки из файла
# in_poetry.txt - имя входного файла
# out_opoetry.txt - имя выходного
with open("in_poetry.txt", encoding='utf-8') as a: #если не указывать кодировку будет ошибка
    #print(a.read())
    #пустая строка
    with open("out_poetry.txt", 'a', encoding='utf-8') as out: # ключ 'а' показывает, что мы добавляем строки в конец (append)
        for line in filter(lambda x: x != '\n', a): 
            out.write(line)
            
#with open("out_poetry.txt", encoding='utf-8') as out:
   # print(out.read())



# for i in a:
#     if 
# while True:
#     s = str(input())
#     if s == 'Конец' or s == 'конец':
#         break
#     k = 0
#     for x in s:
#         if x in 'аеёиоуыэюя':
#             k = k + 1
#     print(k)

print('\\' * 5, 'FINISH', '/' * 5)