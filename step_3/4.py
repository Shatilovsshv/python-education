#Реализовать список месяцев в году, но так, чтобы каждому времени года соотвествовал другой список(испо же список ользуя этотставить только список с месяцями лета)
winter = ['december', 'january', 'february']
summer = ['june', 'july', 'august']
spring = ['march', 'april', 'may']
autumn = ['september', 'october', 'november']

seasons = [winter, summer, spring, autumn]
del seasons[0]
del seasons[1]
del seasons[1]

print(seasons)