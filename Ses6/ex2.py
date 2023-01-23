# se da o lista, sa se afiseze primul si ultimul element impar din lista
# de facut cu un singur for!!
lista = [32, 12, 99, 5, 1, 4, 21, 4, 8]
primul_impar = 0
ultimul_impar = 0
nr_impare = []

for x in range(0,len(lista) -1):
    if lista[x] % 2 == 1:
        nr_impare.append(lista[x])
primul_impar = nr_impare[0]
ultimul_impar = nr_impare[len(nr_impare)-1]
print(primul_impar, ultimul_impar)

# print(len(lista))
# for x in range(len(lista) - 1, -1, -1):
#     if lista[x] % 2 == 1:
#         ultimul_impar = lista[x]
#         break
# for y in range(0, len(lista)):
#     if lista[y] % 2 == 1:
#         primul_impar = lista[y]
#         break
# print("Primul nr impar este:", primul_impar)
# print("Ultimul nr impar este:", ultimul_impar)

# x = len(lista) - 1
# while x >= 0:
#     if lista[x] % 2 == 1:
#         print(lista[x])
#         break
#     x -= 1

# y = 0
# while y <= x:
#     if lista[y] % 2 == 1:
#         print(lista[y])
#         break
#     y += 1
