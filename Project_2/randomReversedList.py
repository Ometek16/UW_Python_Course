from random import randint

lista = [randint(1, 1000) for _ in range(100)]

print(lista[::-1])