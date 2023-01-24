# se citeste de la utilizator numele unei zile din saptamana
# sa se afiseze a cata zi este ziua citita

# zilele_saptamanii = {
#     "luni": 1,
#     "marti": 2,
#     "miercuri": 3,
#     "joi": 4,
#     "vineri": 5,
#     "sambata": 6,
#     "duminica": 7
# }

# x = input("Introdu numele unei zile din saptamana: ")
# x = x.lower()
# if  x in zilele_saptamanii:
#     print(zilele_saptamanii[x])
# else:
#     print("Nu ai intronus numele zilei corect!")


# # for i in zilele_saptamanii:
# #     if i == x:
# #         print (zilele_saptamanii[i])

#EX2
#se citeste de la utilizator un text
#sa se afiseze frecventa fiecarei vocale din text 

#ex: ana are abracadabra

# vocale = 'aeiou'
# frecventa = {}
# text = input("Introduceti un text: ")
# text = text.lower()
# for x in text:
#     if x in vocale:
#         if x in frecventa:
#             frecventa[x] = frecventa[x] + 1
#         else:
#             frecventa[x] = 1

# print(frecventa)

#EX3
# se da o lista de cuvinte
# sa se calculeze frecventa fiecarui cuvant

# lista = ["ana", "are", "mere", "ana", "curs", "abracadabra", "mere", "robert", "intro", "curs", "mere"]

# frecventa = {}

# for x in lista:
#     if x in frecventa:
#         frecventa[x] = frecventa[x] + 1
#     else:
#         frecventa[x] = 1

# print(frecventa)

#EX4
# se citeste n un nr nat urmat de n perechi de forma produs cantitate
# sa se organizeze lista de cumparaturi si sa se afiseze cate produse de ficare fel trebuie cumparate

n = int(input("introdu nr de perechi: "))

lista_finala = {}

for i in range(0, n):
    produs = input("")
    bucati = int(input(""))
    if produs in lista_finala:
        lista_finala[produs] += bucati
    else:
        lista_finala[produs] = bucati
print(lista_finala)
