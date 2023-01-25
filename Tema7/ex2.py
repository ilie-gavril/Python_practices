# Scrieti o functie distincte(lista) care primeste ca parametru o lista de elemente (pot fi numere, stringuri) si returneaza o lista noua care contine doar elementele distincte din lista (fara duplicate), in aceeasi ordine ca in lista initiala.

# Nota: aceasta ar trebuie sa fie o lista nou construita, iar lista initiala sa ramana neschimbata.

def distincte(lista):
    lista_distincte = []
    for x in lista:
        if x not in lista_distincte:
            lista_distincte.append(x)
    return lista_distincte
    
numere = [3, 5, 2, 5, 3, 7]
print(distincte(numere))  # afiseaza: [3, 5, 2, 7]
print(numere)
print(distincte(['aa', 'bb', 'aa', 'cc']))
