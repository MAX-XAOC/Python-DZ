num_init = int(input('Введите целое положительное число: '))
max = num_init % 10
num = num_init

while num > 0:
    digit = num % 10
    if digit > max:
        max = digit

    if digit == 9:
        break

    num =num // 10
    print(num)
print(f"Самая большая цифра в числе {num_init} = {max}")
