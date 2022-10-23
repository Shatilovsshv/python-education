#Вывести строку используя метод подстановки
how_much = 1000
name = 'Василий'
letter = (70 * 'к')

message = '%s чертей, %sаналья!%s снова получил двойку,%s как так получилось?'

print(message % (how_much, letter, name, name))
