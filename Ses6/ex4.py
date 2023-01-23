#se citeste un text de la consola 
#sa se afiseze cate vocale contine textul

# text = input("")
# vocale = "aeiou"
# nr_vocale = 0
# for caracter in text:
#     if caracter in vocale:
#         nr_vocale = nr_vocale + 1
# print(nr_vocale)

# se citeste un text de la consola, sa se afiseze cate consoane are textul

text = input("")
vocale = "aeiou"
nr_consoane = 0
for caracter in text:
    if caracter not in vocale and caracter.isalpha():
        nr_consoane = nr_consoane + 1
print(nr_consoane)
