t = input("Introdu un text: ")

def capete(text):
    if len(text) < 2:
        return text
    prima_ultima = text[0] + text[len(text)-1]
    return prima_ultima
# print(capete(t))

def fara_capete(text):
    if len(text) < 3:
        return text
    text_final = text.lstrip(text[0]).rstrip(text[-1]) 
    return text_final
print(fara_capete(t))

