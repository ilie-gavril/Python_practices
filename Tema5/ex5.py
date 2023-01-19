import os

def incepe_cu(text, litera):
  text = str(text.casefold())
  litera = str(litera)
  if len(text) > 0 and litera == text[0]:
      return True
  else:
      return False
  return False
  
def termina_cu(text, litera):
  text = str(text.casefold())
  litera = str(litera)
  if len(text) > 0 and litera == text[len(text) - 1]:
    return True
  else:
    return False
  return False

def afiseaza_cuvintele_cu(prima_litera, ultima_litera):
  fisier = open("Tema5/data/words_ro.txt", "r")
  cuvant_final = []
  for x in fisier:
    cuvant_verificat = x.strip()
    if incepe_cu(cuvant_verificat, prima_litera) and termina_cu(cuvant_verificat, ultima_litera):
      cuvant_final.append(cuvant_verificat)
  return cuvant_final

