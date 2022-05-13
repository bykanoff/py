hello = {
        'ru': 'Добрый день',
        'en': 'Good day',
        'de': 'Guten tag',
        'dk': 'God dag',
        'default': 'Unknow language'
        }
s = input('Введите код: ')
greet = hello.get(s, hello['default'])
print(greet)