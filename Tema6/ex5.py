# lista = ["ana", "andreea", "sternocleidomastoidian", "ilie"]

def cel_mai_lung(lista_cuvinte):
    cuvant = lista_cuvinte[0]
    if len(lista_cuvinte) == 0:
        return ""
    if len(lista_cuvinte) == 1:
        return lista_cuvinte[0]
    for x in range(len(lista_cuvinte)):
        if len(lista_cuvinte[x]) > len(cuvant):
            cuvant = lista_cuvinte[x]
    return cuvant    

cuvant = cel_mai_lung(['A', 'fost', 'odata', 'ca', 'niciodata', 'o', 'rata'])
print(f'Cel mai lung: {cuvant}')  # afiseaza: Cel mai lung: niciodata

cuvant = cel_mai_lung([""])  # empty list
print(f'Cel mai lung: {cuvant}')  # afiseaza: Cel mai lung:


def cel_mai_lung_din_fisier():
    fisier = open("Tema6/data/words_ro.txt", "r")
    lista = []
    for x in fisier:
        x = x.strip()
        lista.append(x)
    return cel_mai_lung(lista)
    # cuvant = lista[0]
    # for i in range (0, len(lista)):
    #     if len(lista[i]) > len(cuvant):
    #         cuvant = lista[i]
    # return cuvant

cuvant = cel_mai_lung_din_fisier()
print(f'Cel mai lung din fisier: {cuvant} ({len(cuvant)} litere)')