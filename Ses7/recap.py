# se da o lista de numere, sa se calculeze suma elementelor impare din lista

lista = [32, 12, 99, 5, 1, 4, 21, 24]
# 
# def suma_pare(lista):
#     suma = 0
#     for x in range (0, len(lista) -1 ):
#         if lista[x] % 2 != 0:suma = suma + lista[x]

# print(suma)

# se da o lista de numere 
# sa se calculeze si sa se afiseze cel mai mare element din lista


cel_mai_mare = lista[0]

for x in lista:
    if x > cel_mai_mare:
        cel_mai_mare = x

print(cel_mai_mare)

#se da o lista de numere
# sa se afiseze 'da' daca toate elementele din lista sunt pare, respectiv 'nu' in caz contrar
pare = []
for x in lista:
    if x % 2 == 0:
        pare.append(x)
    else:
        break
if len(pare) == len(lista):
    print("da")
else:
    print ("nu")

    