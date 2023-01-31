def anagrame(cuvant1, cuvant2):
    litere_cuvant1 = []
    litere_cuvant2 = []
    for x in cuvant1:
        litere_cuvant1.append(x)
    litere_cuvant1.sort()
    for y in cuvant2:
        litere_cuvant2.append(y)
    litere_cuvant2.sort()
    if litere_cuvant1 == litere_cuvant2:
        return True
    else:
        return False
    
print(anagrame('intrau', 'ruinat'))
print(anagrame('baac', 'cabb')) 

def anagrame_pentru(cuvant):
    fisier = open("Tema6/data/words_ro.txt", "r")
    fisier_deschis = fisier.read().split("\n")
    lista_cuvinte = []
    lista_anagrame = []
    for x in fisier_deschis:
        lista_cuvinte.append(x.split())
    for y in range(0, len(lista_cuvinte)):
        cuvant2 = ''.join(lista_cuvinte[y])
        if anagrame(cuvant, cuvant2):
            lista_anagrame.append(cuvant2)
    return lista_anagrame

print(anagrame_pentru("intrau"))
print(anagrame_pentru('barzi')) 
print(anagrame_pentru('altitudine'))
print(anagrame_pentru('acasa'))
print(anagrame_pentru('programator'))