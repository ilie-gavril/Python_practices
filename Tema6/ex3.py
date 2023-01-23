nr_cuvinte = int(input("numar cuvinte: "))
lista = []

for i in range (0, nr_cuvinte):
    cuvinte = input("introduceti cuvintele: ")
    lista.append(cuvinte)


# cuvinte = ['mere', 'bere', 'andreea','pere', 'codrin', 'codrin', '', 'alexandra', 'liviu', 'loredana', 'ilie', 'ilie']

def gasire_duplicate(lista_cuvinte):
    cuvant_de_comparat = []
    duplicat = ''
    pozitie = [] 
    for i in range (0, len(lista_cuvinte)):
            if lista_cuvinte[i] in cuvant_de_comparat:
                duplicat = lista_cuvinte[i]
                pozitie.append(i)
                for x in range(0, (len(lista_cuvinte) - i)):
                    if lista_cuvinte[x] == duplicat:
                        pozitie.append(x)
                        pozitie.reverse()
                        print("Am gasit o valoare duplicata:", duplicat, "(pe pozitiile:", *pozitie ,")")
                    break
                break
            else:
                cuvant_de_comparat.append(lista_cuvinte[i])
            if cuvant_de_comparat == lista_cuvinte:
                print("Nu contine nici o valoare duplicata") 
gasire_duplicate(lista)
# gasire_duplicate(['aa', 'bb', 'cc', 'aa'])
# gasire_duplicate(['aa', 'bb', 'cc', 'dd'])