revenue = float(input("Введите значение выручки: "))
costs = float(input("Введение значение издержек: "))
result = revenue - costs
if result > 0:
    print(f"Пока вы с прибылью {result} ")
    print(f"Рентабельность выручки: {result / revenue:.3f}")
    persons =int(input("Какова численность сотрудников фирмы? "))
    print(f"Прибыль на одного сотрудника: {result / persons:.3f}")
elif result < 0:
    print(f"Увы, вы работаете с убытком {-result}")