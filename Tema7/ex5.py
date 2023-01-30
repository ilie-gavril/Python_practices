preturi_produse = {'banane': 0.99, 'lapte': 1.5, 'paine': 1.2, 'whisky': 4.9}
numar_produse = {'lapte': 2, 'paine': 1, 'banane': 3, 'miere': 10}

def afiseaza_bon(preturi_produse, numar_produse):
    total_buc = 0
    total_pret = 0
    print("Produse cumparate:")
    for x in preturi_produse:
        if x in numar_produse:
            sub_total = float(preturi_produse[x] * numar_produse[x])
            total_buc += numar_produse[x]
            total_pret += sub_total
            print("- ", x, ":", preturi_produse[x], "x", numar_produse[x], "= {:.2f}".format(sub_total))
    print("TOTAL:", total_buc, "produse = ", "{:.2f}".format(total_pret), "ron")
afiseaza_bon(preturi_produse, numar_produse)