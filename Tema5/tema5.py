import ex1
import ex2
import ex3
import ex4
import ex5

#<-----------RULARE----------->
  
print("Ce exercitiu vrei sa rulezi?\n EX1 - scrie ex1\n EX2 - scrie ex2\n EX3 - scrie ex3\n EX4 - scrie ex4\n EX5 - scrie ex5 \nDaca nu scrii nimic programul va lua sfarsit!!")

to_run = input("Introdu excercitiul aici:")
if to_run == "ex1":
  ex1.citeste_intreg_pozitiv()
if to_run == "ex2":
  print("Valoarea primei puteri peste cand baza este 3 si limita 0:", ex2.prima_putere_peste(3,0))
  print("Valoarea primei puteri peste cand baza este 2 si limita 1020:", ex2.prima_putere_peste(2,1020))
  print("Valoarea primei puteri peste cand baza este 2 si limita 1025:", ex2.prima_putere_peste(2,1025))
  print("Valoarea primei puteri peste cand baza este 7 si limita 10000:", ex2.prima_putere_peste(7,10000))
if to_run == "ex3":
  ex3.simulare(1000, 10, 1500)
  ex3.simulare(1000, 10, 1500)
  ex3.simulare(1000, 8, 3600)
  ex3.simulare(1000, 0.5, 1500)
  ex3.simulare(1000, 10, 900)
if to_run == "ex4":
  print("A.")
  print(ex4.contine('abcde', 'b'))
  print(ex4.contine('abBbe', 'b'))
  print(ex4.contine('abcde', 'x'))
  print(ex4.contine('', 'x'))
  print("B.")
  print(ex4.aparitii('aabcdeef', 'e'))  # afiseaza: 2
  print(ex4.aparitii('aabcdeef', 'y'))  # afiseaza: 0
  print(ex4.aparitii('', 'y'))  # afiseaza: 0
  print(ex4.aparitii('Andreea', 'a')) 
  print("C.")
  print(ex4.numar_vocale('A fost odata un emir..'))
if to_run == "ex5":
  print("A.")
  print(ex5.incepe_cu('bax', 'b'))
  print(ex5.incepe_cu('bax', 'a')) 
  print(ex5.incepe_cu('', 'a'))  
  print(ex5.incepe_cu('a', ''))
  print("B.")
  print(ex5.termina_cu('bax', 'x'))  # afiseaza: True
  print(ex5.termina_cu('bax', 'y'))  # afiseaza: False
  print(ex5.termina_cu('', 'a'))  # afiseaza: False
  print("C.")
  print("Cuvintele care incep cu a si se termina in v:")
  print(*ex5.afiseaza_cuvintele_cu('a','v'), sep = '\n')
  print("Numar cuvinte gasite:", len(ex5.afiseaza_cuvintele_cu('a', 'v')))
else: 
    print("\nProgramul a luat sfarsit!")