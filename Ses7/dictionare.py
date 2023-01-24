#dictionare 
# liste indexate cu text

elev = {
    "nume": "Gavril",
    "prenume": "Ilie",
    "media": 5
}

print(elev["nume"])

for x in elev:
    print(x, "=>", elev[x])


elev["curs"] = "IP"

print(elev)