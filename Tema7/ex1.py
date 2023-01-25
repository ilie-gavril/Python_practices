def analizeaza_note(lista_note):
    catalog = {}
    if len(lista_note) == 0:
        return "Eroare: nu exista note de analizat"
    for i in range(0, len(lista_note)):
        if type(lista_note[i]) == str:
            return "Eroare: nu exista note de analizat"
    if len(lista_note) == 1:
        if 1 <= lista_note[0] <= 10:
            catalog["min"] = lista_note[0]
            catalog["max"] = lista_note[0]
            catalog["medie"] = lista_note[0] / len(lista_note)
            return catalog
        else: 
            return "Eroare: nu exista note de analizat"
    if lista_note[0] > lista_note[1]:
        catalog["min"] = lista_note[1]
        catalog["max"] = lista_note[0]
    else:
        catalog["min"] = lista_note[0]
        catalog["max"] = lista_note[1]
    suma = lista_note[0] + lista_note[1]
    for x in range(2, len(lista_note)):
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
print(analizeaza_note([]))
print(analizeaza_note([3, 4,"A", 5, "S"]))
print(analizeaza_note([8]))
print(analizeaza_note([7, 8, 5, 9]))
print(analizeaza_note([7, 8, 5, 9,-1]))
print(analizeaza_note([7, 8, 5, 9, 11]))
