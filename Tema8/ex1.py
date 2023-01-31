import random

nume_jucatori = input("Introduceti numele fiecaruia separate de un spatiu: ")
def amestecate(linie_nume):
    lista_jucatori = linie_nume.split()
    ordine_noua = lista_jucatori.copy()
    random.shuffle(ordine_noua)
    numaratoare = 0
    for x in ordine_noua:
        numaratoare += 1
        print(f"{numaratoare}.{x}")
    return ordine_noua
       
def echipe_random(linie_nume):
    jucatori = linie_nume.split()
    numar_jucatori = len(jucatori)
    numar_echipe = int(input("Introdu nr de echipe: "))
    while numar_jucatori > 0 and numar_echipe > 0:
        echipa = random.sample(jucatori,int(numar_jucatori/numar_echipe))
        for x in echipa:
            jucatori.remove(x)
        numar_jucatori -= int(numar_jucatori/numar_echipe)
        numar_echipe -= 1
        print(*echipa)

amestecate(nume_jucatori)
echipe_random(nume_jucatori)