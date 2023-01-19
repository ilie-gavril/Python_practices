def citeste_intreg_pozitiv():
  a = input("Introduceti un numar:")
  while a.isdigit() == False:
    a = input("Introduceti un numar:")
    if a.isdigit() == True:
      print("Numarul final pozitiv este:", a)
      return a
  print("Numarul final pozitiv este:", a)
  return a