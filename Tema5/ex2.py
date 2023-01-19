def prima_putere_peste(baza, limita):
  baza = int(baza)
  limita = int(limita)
  putere = 0
  valoarea_puterii = baza ** putere
  while valoarea_puterii < limita:
    valoarea_puterii = baza ** putere
    putere = putere + 1
    #print(valoarea_puterii)
  return valoarea_puterii