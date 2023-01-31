import random
import functii
# fisier_cuvinte = open("tema8/spanzuratoarea/words_ro.txt", "r")
# lista_cuv = fisier_cuvinte.read().split("\n")
# lista_cuvinte = []
# cuvinte_grele = functii.cele_mai_lungi_din_fisier()
# for x in lista_cuv:
#         lista_cuvinte.append(x.split())
logo = open("tema8/spanzuratoarea/logo.txt", "r")
print(logo.read())

print("Poti alege din 3 nivele de dificultate! Nivel 1 => 1 ; Nivel 2 => 2 ; Nivel 3 => 3")
numar_nivel = int(input("Scrie aici > "))
cuvant_ales = random.choice(functii.alege_nivel(numar_nivel))
cuvant_ales = cuvant_ales[0]
functii.demascare_cuvant(cuvant_ales)

# fisier_cuvinte = open("tema8/spanzuratoarea/words_ro.txt", "r")
# lista_cuvinte = fisier_cuvinte.read().split("\n")
# lista_finala = []
# for x in lista_cuvinte:
#     if  3 < len(x) < 5:
#         lista_finala.append(x.split())
# fisier_cuvinte.close()

# print(lista_finala)

# print(functii.alege_nivel(numar_nivel))

# if nivel_greu.lower() == "da":
#     cuvant_ales = random.choice(cuvinte_grele)
#     functii.demascare_cuvant(cuvant_ales)
# elif nivel_greu.lower() == "nu": 
#     cuvant_ales = random.choice(lista_cuvinte)
#     cuvant_ales = cuvant_ales[0]
#     functii.demascare_cuvant(cuvant_ales)
# else:
#     print("Ceao!")
# print(cuvant_ales)
# print(*functii.mascare_cuvant(cuvant_ales))
