while True:
    days = 1
    start = float(input('Начальный результат: '))
    finish = float(input('Финальный результат: '))
    if start <= 0 or finish < 0:
        print('Начальное значение !=0')
    else:
        while start < finish:
            start *= 1.1
            days += 1
        print(f'Результат появится на {days} день')