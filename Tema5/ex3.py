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
