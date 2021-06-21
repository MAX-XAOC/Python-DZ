def personal_inf(**kwargs):
    return ' '.join(kwargs.values())


name = input('Введите имя : ')
surname = input('Введите фамилию :')
year_of_birth = input('Введите год рождения : ')
city_of_residence = input('Введите город проживания:')
email = input('Введите email : ')
phone = input('Введите телефон : ')

print(personal_inf(name=name, surname=surname, year_of_birth=year_of_birth, city_of_residence=city_of_residence, email=email, phone=phone))