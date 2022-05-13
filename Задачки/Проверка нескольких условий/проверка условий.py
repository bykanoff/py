print("*" * 8, "START", "*" * 8, "\n")


while True:
    print("""Выберите ваш браузер:
1 - Google Chrome
2 - FireFox
3 - MS Edge
4 - Opera
5 - Safary
6 - Other""")
    
    browser = input("Какой браузер у вас:\n");
    
    if browser == "q" or browser == "Q":
        print("*" * 5, "The End", "*" * 5)
        break
    elif not browser.isdigit():
        print("-" * 5, "Выберите значение из списка", "-" * 5,"\n")
        continue
    
    
    browser = int(browser)

    if browser == 1:
        print("Your browser is Google Chrome \n")
    elif browser == 2:
        print("Your browser is Firefox \n")
    elif browser == 3:
        print("Your browser is MS Edge \n")
    elif browser == 4:
        print("Your browser is Opera \n")
    elif browser == 5:
        print("Your browser is Safary \n")
    elif browser == 6:
        print("You have Other Browser \n")
    else:
        print("-" * 5, "Выберите браузер из списка", "-" * 5,"\n")


