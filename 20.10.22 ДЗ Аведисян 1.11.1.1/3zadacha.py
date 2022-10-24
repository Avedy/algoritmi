# O(n)


def kamni(jewels, stones):
    chet=0 # Вводим счётчик наших камней среди драгоценных
    for i in jewels: # Проходимся по элементам драгоценных камней
        for j in stones: # Проходимся по нашим камням
            if i==j: # Если наш камень есть в драгоценных камнях, то добавляем в счётчик 1
                chet=chet+1
    return chet


print("У нас всего", kamni(jewels="aA", stones="zaAaa"), "драгоценных камней")