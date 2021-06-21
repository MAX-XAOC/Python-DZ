reiting_spisok = [9, 9, 8, 8, 7, 6, 6, 5, 5, 3, 2, 1]
reiting_number = int(input('Введите натуральное число из рейтинга : '))
i = 0
for n in reiting_spisok:
    if reiting_number <= n:
        i += 1
reiting_spisok.insert(i, float(reiting_number))
print(reiting_spisok)
