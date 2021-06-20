a = input('Введите элементы через пробелы: ').split()
i = 0
print(f'Начальный список {a}')
while i + 1 < len(a):
    if i % 2 == 0:
        a.insert(i, a.pop(i + 1))
    i += 1
print(f'Последний список {a}')