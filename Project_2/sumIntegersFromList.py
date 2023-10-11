lista = [1, 10, "ugabuga", 5.0]

suma = 0

for elem in lista:
    if (isinstance(elem, int)):
        suma += elem

print(suma)