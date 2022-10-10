#Реализовать список месяцев в году, но так, чтобы каждому времени года соотвествовал другой список(испо же список ользуя этотставить только список с месяцями лета)
winter = ['декабрь', 'январь', 'февраль']
summer = ['june', 'july', 'august']
spring = ['march', 'april', 'may']
autumn = ['september', 'october', 'november']

seasons = winter
seasons.append(summer)
seasons.append(spring)
seasons.append(autumn)
del seasons[0]
del seasons[1]
del seasons[2]
del seasons[2]
del seasons[0]

print(seasons)

