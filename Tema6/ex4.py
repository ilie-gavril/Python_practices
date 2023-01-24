def e_alfabetic(cuvant):
    for x in range(0, len(cuvant)-1):
        if cuvant[x] > cuvant[x+1]:
            return False
    return True       
    
print(e_alfabetic("aefgz"))
print(e_alfabetic('aefgc'))
print(e_alfabetic('abcdefgz'))

def cuvinte_alfabetice_din_fisier():
    fisier = open("Tema6/data/words_ro.txt", "r")
    cuvant_verificat = []
    cuvinte_alfabetice = []
    cuvinte_gasite = 0
    for x in fisier:
        cuvant_verificat = x.strip()
        if e_alfabetic(cuvant_verificat):
            cuvinte_alfabetice.append(cuvant_verificat)
            cuvinte_gasite += 1
    print("Cuvintele alfabetice din fisier:", *cuvinte_alfabetice, sep='\n')
    print( "Total cuvinte gasite: ", cuvinte_gasite)


cuvinte_alfabetice_din_fisier()