# Сложность O(n)
# Чтобы получить число1 в Системе Счисления числа2, нужно, чтобы число1 при помощи деления на число2, стало меньше чем число2


def base(n,k):
    digit=0 # Вводим счётчик суммы
    while n!=0: # Нужно чтобы первое число, которое в 10 СС не было равно 0
        digit+=(n%k) # Делим с остатком число1 на число2, чтобы вынести вторую часть числа1 для СС числа2, добавляем остаток от деления в счётчик суммы
        n=n//k # Делим число1 нацело на число2, чтобы вынести первую часть числа1 для СС числа2
    return digit+n # Складываем наш счётчик и первую часть числа1 для СС числа2


print(base(34,6))