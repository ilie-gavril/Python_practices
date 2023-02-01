import random
import functii

logo = open("tema8/spanzuratoarea/logo.txt", "r")
print(logo.read())

print("Poti alege din 3 nivele de dificultate! Nivel 1 => 1 ; Nivel 2 => 2 ; Nivel 3 => 3")
numar_nivel = functii.numar_nivel()
cuvant_ales = random.choice(functii.alege_nivel(numar_nivel))
cuvant_ales = cuvant_ales[0]
functii.demascare_cuvant(cuvant_ales)