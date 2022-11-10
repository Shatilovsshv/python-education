money = int(input())
if money <= 100:
    print("слишком мало")
elif money > 100 and money < 500:
    print("мало")
elif money >= 500 and money <= 1000:
    print("нормально")
elif money > 1000 and money <= 5000:
    print("много")
elif money > 5000:
    print("больше чем много")