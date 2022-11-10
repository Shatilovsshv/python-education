#По приколу добавил ручной ввод
twinkies = int(input())
if twinkies <= 100:
    print("Слишком мало")
elif twinkies > 100 and twinkies < 500:
    print("Нормально")
elif twinkies >= 500:
    print("Cлишком много")