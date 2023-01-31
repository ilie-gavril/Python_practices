def cifreaza(text, deplasament):
    caracter = ''
    text_criptat = ''
    for x in range(len(text)):
        caracter = text[x]
        if caracter == " ":
            text_criptat += " "
        elif (caracter.isalpha() == False):
            text_criptat += caracter
        elif (caracter.isupper()):
            text_criptat += chr((ord(caracter) + deplasament - 65) % 26 + 65)    
        else:
            text_criptat += chr((ord(caracter) + deplasament - 97) % 26 + 97)
    return text_criptat

def descifreaza(text, deplasament):
    caracter = ''
    text_decriptat = ''
    for x in range(len(text)):
        caracter = text[x]
        if caracter == " ":
            text_decriptat += " "
        elif (caracter.isalpha() == False):
            text_decriptat += caracter
        elif (caracter.isupper()):
            text_decriptat += chr((ord(caracter) - deplasament - 65) % 26 + 65)    
        else:
            text_decriptat += chr((ord(caracter) - deplasament - 97) % 26 + 97)
    return text_decriptat

def cifrare_fisier(nume_fisier, deplasament):
   continut_fisier = nume_fisier.read().split('\n')
   criptare = []
   for x in continut_fisier:
    criptare.append(cifreaza(x.strip(), deplasament))
   fisier_exportat = open("tema8/files/mesaj.txt_encoded", "w")
   for x in criptare:
    cuvinte_exportate = x + "\n"
    fisier_exportat.write(cuvinte_exportate) 

def descifrare_fisier(nume_fisier, deplasament):
   continut_fisier = nume_fisier.read().split('\n')
   decriptare = []
   for x in continut_fisier:
    decriptare.append(descifreaza(x.strip(), deplasament))
   fisier_exportat = open("tema8/files/mesaj.txt_encoded_decoded", "w")
   for x in decriptare:
    cuvinte_exportate = x + "\n"
    fisier_exportat.write(cuvinte_exportate) 


fisier_initial = open("tema8/files/mesaj.txt", "r")
fisier_criptat = open("tema8/files/mesaj.txt_encoded", "r")

cifrare_fisier(fisier_initial, 3)
descifrare_fisier(fisier_criptat, 3)

fisier_initial.close()
fisier_criptat.close()


# print(cifreaza('abcxyz 123?!', 3))
# print(descifreaza('defabc 123?!', 3))

# print(cifreaza('trimite intariri, 3 cohorte!', 13))
# print(descifreaza(cifreaza('trimite intariri, 3 cohorte!', 13), 13))