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
