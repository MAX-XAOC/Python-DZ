spisok = ['String', [1, 2], 5, 1.1, True, None,
        TypeError, (-1 + 0j),{1, 111},
        (1, 2, 2.1), {1: 'one', 2: 'two',3: 'free'},
        range(100) ]

for i, item in enumerate(spisok, 1):
    print(f"{i}) {item} - {type(item)}")
