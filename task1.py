a=int (input('Введите ваш возраст: '))

def age(a):
    if a < 2:
        return None
    elif 2 <= a <= 6:
        return 'Вы ходите в детский сад'
    elif 6 < a <= 17:
        return 'Вы учитесь в школе'
    elif 17 <= a <= 22:
        return 'Вы учитесь в ВУЗе'
    elif 22 < a <= 65:
        return 'Вы работаете'
    else:
        return None

print (age(a))


