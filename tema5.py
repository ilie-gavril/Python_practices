#Ex.1
def citeste_intreg_pozitiv():
  a = input("Introduceti un numar:")
  while a.isdigit() == False:
    a = input("Introduceti un numar:")
    if a.isdigit() == True:
      return a
  return a
#Ex.2
  
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
#Ex.3
  
def simulare(suma_initiala, procent_dobanda, suma_dorita):
  suma_initiala = int(suma_initiala)
  procent_dobanda = float(procent_dobanda)
  suma_dorita = int(suma_dorita)
  dobanda = suma_initiala * (procent_dobanda / 100)
  dobanda_acumulata = dobanda
  suma_acumulata = suma_initiala
  ani = 0
  print("Parametrii simulare: ""suma_initiala: ""{:.2f}".format(suma_initiala), "procent_dobanda: ""{:.2f}".format(procent_dobanda),"suma_dorita: ""{:.2f}\n".format(suma_dorita))
  while suma_acumulata <= suma_dorita:
    ani = ani + 1
    dobanda_acumulata = suma_acumulata * (procent_dobanda / 100)
    suma_initiala = suma_acumulata
    suma_acumulata = suma_acumulata + dobanda_acumulata
    print("- an:", ani, "Suma initiala: ""{:.2f}".format(suma_initiala),"Dobanda: ""{:.2f}".format(dobanda_acumulata), "Noua suma: ""{:.2f}".format(suma_acumulata))
  print("\n Te poti pensiona linistit in: ", ani, "ani!")
  return ani

#Ex.4
def contine(text, litera):
  text = str(text.casefold())
  litera = str(litera)
  for litera_iteratie in text:
      if litera_iteratie == litera:
        return True
  return False

def aparitii(text, litera):
  text = str(text.casefold())
  litera = str(litera)
  numaratoare_litera = 0
  for comparatie_litera in text:
    if comparatie_litera == litera:
      numaratoare_litera = numaratoare_litera + 1
  return numaratoare_litera

def numar_vocale(text):
  text = text.casefold()
  i = 0
  numaratoare = 0
  vocale = 'aeiou'
  while i < len(text):
    if contine(vocale,text[i]):
      numaratoare = numaratoare + 1
    i = i + 1
  return numaratoare

#Ex.5
  
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
  fisier = open("data/words_ro.txt", "r")
  cuvant_final = []
  for x in fisier:
    cuvant_verificat = x.strip()
    if incepe_cu(cuvant_verificat, prima_litera) and termina_cu(cuvant_verificat, ultima_litera):
      cuvant_final.append(cuvant_verificat)
  return cuvant_final



#<-----------RULARE----------->
  
print("Ce exercitiu vrei sa rulezi?\n EX1 - scrie ex1\n EX2 - scrie ex2\n EX3 - scrie ex3\n EX4 - scrie ex4\n EX5 - scrie ex5 \nDaca nu scrii nimic programul va lua sfarsit!!")

to_run = input("Introdu excercitiul aici:")

if to_run == "ex1":
  print(citeste_intreg_pozitiv())
if to_run == "ex2":
  print("Valoarea primei puteri peste cand baza este 3 si limita 0:", prima_putere_peste(3,0))
  print("Valoarea primei puteri peste cand baza este 3 si limita 0:", prima_putere_peste(2,1020))
  print("Valoarea primei puteri peste cand baza este 3 si limita 0:", prima_putere_peste(2,1025))
  print("Valoarea primei puteri peste cand baza este 3 si limita 0:", prima_putere_peste(7,10000))
if to_run == "ex3":
# simulare(1000, 10, 1500)
# simulare(1000, 10, 1500)
  simulare(1000, 8, 3600)
# simulare(1000, 0.5, 1500)
# simulare(1000, 10, 900)
if to_run == "ex4":
  print("A.")
  print(contine('abcde', 'b'))
  print(contine('abBbe', 'b'))
  print(contine('abcde', 'x'))
  print(contine('', 'x'))
  print("B.")
  print(aparitii('aabcdeef', 'e'))  # afiseaza: 2
  print(aparitii('aabcdeef', 'y'))  # afiseaza: 0
  print(aparitii('', 'y'))  # afiseaza: 0
  print(aparitii('Andreea', 'a')) 
  print("C.")
  print(numar_vocale('A fost odata un emir..'))
if to_run == "ex5":
  print("A.")
  print(incepe_cu('bax', 'b'))
  print(incepe_cu('bax', 'a')) 
  print(incepe_cu('', 'a'))  
  print(incepe_cu('a', ''))
  print("B.")
  print(termina_cu('bax', 'x'))  # afiseaza: True
  print(termina_cu('bax', 'y'))  # afiseaza: False
  print(termina_cu('', 'a'))  # afiseaza: False
  print("C.")
  print("Cuvintele care incep cu a si se termina in v:")
  print(*afiseaza_cuvintele_cu('a','v'), sep = '\n')
  print("Numar cuvinte gasite:", len(afiseaza_cuvintele_cu('a', 'v')))
else: 
    print("\nProgramul a luat sfarsit!")