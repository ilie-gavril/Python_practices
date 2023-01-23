def multiplica(lista_numere, factor):
    for i in range (0, len(lista_numere)):
        lista_numere[i] = (lista_numere[i] * factor)
numere = [2, 5, 1, 7]
multiplica(numere, 3)
print(numere)