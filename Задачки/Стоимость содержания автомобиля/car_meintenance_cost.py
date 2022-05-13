# Расчет стоимости содержания автомобиля
# Ввод значения переменных
service = input("Стоимость ТО: ")
fuel = input("Стоимость топлива: ")
tax = input("Транспортный налог: ")
tuning = input("Тюнинг и прочие доработки: ")
insurance = input("ОСАГО: ")
# Явная инициализация переменных
service = float(service)
fuel = float(fuel)
tax = float(tax)
tuning = float(tuning)
insurance = float(insurance)

total = service + fuel + tax + tuning + insurance

print("Всего: ", total)


