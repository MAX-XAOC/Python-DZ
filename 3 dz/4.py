def my_fun(x, y):
    try:
        x, y = int(x), int(y)
        if x <= 0 or y >= 0:
            return 'Ошибка x должен быть больше 0, а y должен быть меньше 0'
        else:
            resultat = 1
            for _ in range(abs(y)):
                resultat *= 1 / x
            return f'результат возведения x в степень y = {round(resultat, 2)}'
    except ValueError:
        return "работает только с числами."

print(my_fun(3, -3))