print("-" * 5, "Hello friend", "-" * 5, "\n")

# Программа принимает на вход и печатает фразу "Привет, имя пользователя!"

while True:
    a = input("Добрый день, как вас зовут?\nНапишите свое имя: \n")
    if a.isdigit():
        print(f"{a} - это не похоже на имя человека!\n")
        continue
    else:
        print(f"Приятно познакомится, {a}!")
        break