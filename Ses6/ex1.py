# se da o lista de numere
# sa se afiseze nr pare care sunt pe pozitii impare
#         0   1   2  3  4  5   6   7
lista = [32, 12, 99, 5, 1, 4, 21, 24]

# for x in range(0, len(lista)):
#     if x % 2 == 1 and lista[x] % 2 == 0:
#         print(lista[x])

# se da o lista de nr 
# sa se calculeze suma si media aritmetica elementelor din lista

# lista = [32, 12, 99, 5, 1, 4, 21, 24]
suma = 0
for x in range (0, len(lista)):
    suma = suma + lista[x]
media_aritmetica = suma / len(lista)
print(suma)
print(media_aritmetica)