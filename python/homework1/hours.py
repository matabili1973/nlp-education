# Вводится время в секундах
time = int(input('Введите количество секунд:\n'))

# Вычисляется количество часов, минут и секунд
hours = time // 3600
minutes = time // 60 % 60
seconds = time % 60

#Выводится время в формате чч:мм:сс
print('{:0=2}:{:0=2}:{:0=2}'.format(hours, minutes, seconds))
