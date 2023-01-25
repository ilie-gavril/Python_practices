#Scrieti o functie analizeaza_note(lista_note) care primeste ca parametru o lista de numere reprezentand notele unei grupe de studenti (numere intregi, intre 1 si 10) si calculeaza si afiseaza nota minima, maxima si media lor aritmetica.

#Nota: pentru o eficienta mai buna, incercati sa folositi o singura bucla (daca nu reusiti, e acceptabil sa folositi si 2-3 bucle)

def analizeaza_note(lista_note):
    catalog = {}
    if len(lista_note) == 0: #cand lista nu are niciun element
        return "Eroare: nu exista note de analizat"
    for i in range(0, len(lista_note)):
        if type(lista_note[i]) == str:
            return "Eroare: nu exista note de analizat"
    if len(lista_note) == 1: #cand lista are 1 element
        if 1 <= lista_note[0] <= 10: # daca elementul din lista este cuprins intre 1 - 10
            catalog["min"] = lista_note[0]
            catalog["max"] = lista_note[0]
            catalog["medie"] = lista_note[0] / len(lista_note)
            return catalog
        else: 
            return "Eroare: nu exista note de analizat"
    if lista_note[0] > lista_note[1]: #dam valori max si valori mix pentru primele 2 cazuri
        catalog["min"] = lista_note[1]
        catalog["max"] = lista_note[0]
    else:
        catalog["min"] = lista_note[0]
        catalog["max"] = lista_note[1]
    suma = lista_note[0] + lista_note[1]
    for x in range(2, len(lista_note)): #incepem de la al 3-lea element fiindca deja am tratat primele 2 cazuri
        if 1 <= lista_note[x] <= 10:
            if lista_note[x] > catalog["max"]:
                catalog["max"] = lista_note[x]
            elif lista_note[x] < catalog["max"]:
                catalog["min"] = lista_note[x]
        else:
            return "Nu ati introdus o nota valida"
        suma = suma + lista_note[x]
    catalog["medie"] = suma / len(lista_note)
    return catalog

analiza = analizeaza_note([7, 8, 5, 9])
print("Min: ", analiza["min"], "max: ", analiza["max"], "medie:", analiza["medie"])

print(analizeaza_note([]))
print(analizeaza_note([3, 4,"A", 5, "S"]))
print(analizeaza_note([8]))
print(analizeaza_note([7, 8, 5, 9]))
print(analizeaza_note([7, 8, 5, 9,-1]))
print(analizeaza_note([7, 8, 5, 9, 11]))
