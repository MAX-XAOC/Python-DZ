num = 0
try:
    while num != 'A':
        for i in map(int, input(' Введите числа  используя пробел (Для выхода введите A):  ').split()):
            num += i
        print(num)
except ValueError:
    print(num)