import pyperclip
#импортируем модуль
#для красоты вывода добавим ещё несколько команд
print('Текст необходимо скопировать заранее')
print('_' * 40)
s = pyperclip.paste()#команда, позволяющая получить текст из буфера обмена
s = s.replace('\n', '').replace('\r','') #удаляем знаки переноса строк
n1 = len(s)
s = s.replace(' ', '')
n2 = len(s)
print('Количество символов в пробелами: ' +str(n1))
print('Количество символов без пробелов: ' +str(n2))
print('_' * 40)
print(pyperclip.paste())