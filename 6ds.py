def fun(word):
    latin_char = 'slovosdffsdsdfsdfss'
    return word.title() if not set(word).difference(latin_char) else False
word = input('Введите строку из слов разделенных пробелами : ').split()
for w in word:
    resultat = fun(w)
    if resultat:
        print(fun(w), ' ')