import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

HANGMANPICSrev = HANGMANPICS[::-1]

def cele_mai_lungi_din_fisier():
    fisier = open("tema8/spanzuratoarea/words_ro.txt", "r")
    lista = []
    cele_mai_lungi = []
    for x in fisier:
        x = x.strip()
        lista.append(x)
    cuvant = lista[0]
    for x in range(0, len(lista)):
        if len(lista[x]) == len(cuvant):
            cuvant = lista[x]
            cele_mai_lungi.append(cuvant)
        if len(lista[x]) > len(cuvant):
            cuvant = lista[x]
            cele_mai_lungi = []
            cele_mai_lungi.append(cuvant)
    return cele_mai_lungi


def mascare_cuvant(cuvant):
        litere_cuvant = []
        cuvant_mascat = []
        for caracter in cuvant:
            litere_cuvant.append(caracter)
        for x in range(0, len(litere_cuvant)):
            if x == 0 or x == (len(litere_cuvant)-1):
                cuvant_mascat.append(litere_cuvant[x])
            else:
                cuvant_mascat.append("_")
        return cuvant_mascat

def demascare_cuvant(cuvant):
    litere_cuvant = []
    for caracter in cuvant:
        litere_cuvant.append(caracter)
    incercari = 7
    cuvant_demascat = mascare_cuvant(cuvant)
    print(*cuvant_demascat)
    while incercari > 0:
        litera = input("Introdu o litera: ")
        for x in range(1, len(litere_cuvant)-1):
            if litera == litere_cuvant[x]:
                cuvant_demascat[x] = litera
                print(*cuvant_demascat)
            elif litera == cuvant_demascat[x]:
                print("Ai descoperit deja aceasta litera")
                break;
            elif litera not in litere_cuvant:
                incercari -= 1
                print(HANGMANPICSrev[incercari])
                print(*cuvant_demascat)
                print("Mai ai", incercari, "incercari")
                if incercari == 0:
                    print("Ai pierdut! Cuvantul era:", cuvant)
                break;
        if cuvant_demascat == litere_cuvant:
            print("Felicitari! Ai ghicit cuvantul ascuns!")
            break;

def numar_nivel():
    input_nivel = input("Scrie aici > ")
    while type(input_nivel) == str:
        try:
            input_nivel = int(input_nivel)
            return input_nivel
        except ValueError:
            input_nivel = 0
            print("Nu ai introdus un numar valid!")
        

def alege_nivel(numar):
    match numar:
        case 1:
            fisier_cuvinte = open("tema8/spanzuratoarea/words_ro.txt", "r")
            lista_cuvinte = fisier_cuvinte.read().split("\n")
            lista_finala = []
            for x in lista_cuvinte:
                if  3 < len(x) < 5:
                    lista_finala.append(x.split())
            fisier_cuvinte.close()
            print("Ati ales nivelul 1 de dificultate!")
            return lista_finala
        case 2:
            fisier_cuvinte = open("tema8/spanzuratoarea/words_ro.txt", "r")
            lista_cuvinte = fisier_cuvinte.read().split("\n")
            lista_finala = []
            for x in lista_cuvinte:
                if  6 < len(x) < 8:
                    lista_finala.append(x.split())
            fisier_cuvinte.close()
            print("Ati ales nivelul 2 de dificultate!")
            return lista_finala            
        case 3:
            fisier_cuvinte = open("tema8/spanzuratoarea/words_ro.txt", "r")
            lista_cuvinte = fisier_cuvinte.read().split("\n")
            lista_finala = []
            for x in lista_cuvinte:
                if  9 < len(x) < 20:
                    lista_finala.append(x.split())
            fisier_cuvinte.close()
            print("Ati ales nivelul 3 de dificultate!")
            return lista_finala
        case _:
            fisier_cuvinte = open("tema8/spanzuratoarea/words_ro.txt", "r")
            lista_cuvinte = fisier_cuvinte.read().split("\n")
            lista_finala = []
            for x in lista_cuvinte:
                lista_finala.append(x.split())
            fisier_cuvinte.close()
            print("Nu ati ales niciun nivel de dificultate! Veti juca la un nivel aleator!")
            return lista_finala

    
# print(type(cuvant_ales))
# print(cuvant_ales)