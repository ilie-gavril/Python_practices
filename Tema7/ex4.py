def inlocuieste(text, cuvinte_de_inlocuit):
    for x,y in cuvinte_de_inlocuit.items():
            text = text.replace(x, y)
    return text
    
print(inlocuieste('Ana are mere', {'mere': 'cirese', 'Ana': 'Ion'}))
print(inlocuieste('aa bb cc aa dd ee', {'aa': 'A', 'dd': ''}))