 # Проверка на простое ли это число
def is_Prime(n):
    n == 1
    n == 2
    i = 2
    while n % i != 0:
        i += 1
    return i == n