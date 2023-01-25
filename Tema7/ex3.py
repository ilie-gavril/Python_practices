# Scrieti o functie paranteze_corecte(expresie) care primeste ca parametru o expresie (o valoare string) care poate contine paranteze rotunde si diverse alte caractere, si verifica daca parantezele sunt toate corect deschise si inchise.

# Regulile generale pentru a fi corecte:

# toate parantezele trebuie sa aiba pereche (ar trebui sa avem acelasi numar de paranteze deschise si inchise)
# fiecare pereche de paranteze trebuie sa inceapa cu cea deschisa (nu poate sa inceapa cu cea inchisa)
# Functia ar trebui sa intoarca un rezultat de tip boolean: True daca expresia e corecta, False in caz contrar.

def paranteze_corecte(expresie):
    paranteza_deschisa = "("
    paranteza_inchisa = ")"
    nr_paranteze_deschise = 0
    nr_paranteze_inchise = 0
    for x in expresie:
        if x == paranteza_deschisa:
            nr_paranteze_deschise += 1
        if x == paranteza_inchisa:
            nr_paranteze_inchise += 1
        if nr_paranteze_inchise > nr_paranteze_deschise:
            return False
    if nr_paranteze_inchise == nr_paranteze_deschise:
        return True
    else:
        return False


print(paranteze_corecte(''))                  # afiseaza: True
print(paranteze_corecte('abc 12'))            # afiseaza: True
print(paranteze_corecte('abc ()'))            # afiseaza: True
print(paranteze_corecte('x*(y+z), (2+3)'))    # afiseaza: True
print(paranteze_corecte('(1+(2+3))-4'))       # afiseaza: True
print(paranteze_corecte('(.()..((?))..)..'))  # afiseaza: True

print(paranteze_corecte('(..'))         # afiseaza: False
print(paranteze_corecte('..)(..()..'))  # afiseaza: False
print(paranteze_corecte('..()..)'))     # afiseaza: False
print(paranteze_corecte('..()..)('))     # afiseaza: False