# a = int(input("a = "))
# b = int(input("b = "))
# suma = a + b
# diferenta = a - b
# puterea = a ** b
# print(suma, diferenta, puterea)

# def rest(a,b):
#     return a % b

# print(rest(a,b))

# def cuprins(a,b,x):
#     if a < x < b or b < x < a:
#         return 1
#     else:
#         return 0

# print(cuprins(2,7,5))
# print(cuprins(7,2,4))
# print(cuprins(7,2,10))

# sa se scrie o functie numita minim care primeste 2 nr si care returneaza minimul celor 2 numere

# def minim(a,b):
#     if a == b:
#         return "Nr date sunt egale!"
#     if a < b:
#         return a
#     if b < a:
#         return b

# # print(minim(3,6))
# # print(minim(4,2))
# # print(minim(9,9))

# def minim4(a,b,c,d):
#     return minim(minim(a,b),minim(c,d))

# print(minim4(5,4,19,2))
# print(minim4(2,4,19,5))
# print(minim4(5,2,19,4))
# print(minim4(5,10,2,4))


# se citeste un nr n 

# n = int(input("n = "))
# mare = 0
# for x in range(0, n):
#     numar = int(input("numar = "))
#     if mare < numar:
#         mare = numar
# print(mare)

# se de o lista de nr, sa se afiseze cele mai mari 2 elemente din lista

# lista = [32, 12, 99, 32, 1, 4, 21, 4, 8]
# max = 0
# max_2 = 0
# for x in range (0, len(lista)):
#     if max < lista[x]:
#         max = lista[x]
# lista.remove(max)
# for x in range (0, len(lista)):
#     if max_2 < lista[x]:
#         max_2 = lista[x]
# print(max, max_2)

# se da o lista de cuvinte
# sa se afiseze cuvantul cu frecventa cea mai mare

# lista_cuvinte = ["robert", "ilie", "oana", "tudor", "robert", "valentin", "ilie", "ilie"]
# frecventa = {}
# for x in lista_cuvinte:
#     if x in frecventa:
#         frecventa[x] += 1
#     else:
#         frecventa[x] = 1
# max = 0
# cuvant_maxim = ""
# for cuvant in frecventa:
#     if frecventa[cuvant] > max:
#         max = frecventa[cuvant]
#         cuvant_maxim = cuvant

# print(max, cuvant_maxim)

# se da o lista de cuvinte
# sa se calculeze si sa se afiseze cel mai lung cuvant din lista, urmat de lungimea sa

lista_cuvinte = ["robert","abcdefgzjsisdf","ilie", "oana", "tudor", "robert", "valentin", "ilie", "ilie"]

def cel_mai_lung(lista_cuvinte):
    cuvant = lista_cuvinte[0]
    if len(lista_cuvinte) == 0:
        return ""
    if len(lista_cuvinte) == 1:
        return lista_cuvinte[0]
    for x in range(0, len(lista_cuvinte)):
        if len(lista_cuvinte[x]) > len(cuvant):
            cuvant = lista_cuvinte[x]
    return cuvant

print(cel_mai_lung(lista_cuvinte), len(cel_mai_lung(lista_cuvinte)))