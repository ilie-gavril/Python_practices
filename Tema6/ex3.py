cuvinte = ['mere', 'pere', 'bere', 'pere', 'andreea', 'codrin', 'codrin', '', 'alexandra', 'liviu', 'loredana', 'ilie', 'ilie']

def gasire_duplicate(lista_cuvinte):
    cuvant = lista_cuvinte[0]
    duplicat = []
    for x in range(0, len(lista_cuvinte)):
        if cuvant in lista_cuvinte[x]:
            if len(cuvant) > 2:
                duplicat.append(lista_cuvinte[x])
                cuvant = lista_cuvinte[0]
    print(duplicat)

gasire_duplicate(cuvinte)