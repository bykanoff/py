dist = 0 # Расстояние, которое нужно проехать
speed = 0 # Средняя скорость авто, в км/ч

dist = int(input("Расстояние: "))
speed = int(input("Планируемая средняя скорость: "))

time = dist * 60 / speed

print("Время в пути ", time, " минут.")