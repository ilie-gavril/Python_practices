#se dau 2 nr a si b sa se calculeze suma nr pare cuprinse intre a si b

# a = int(input("a ="))
# b = int(input("b ="))
# suma = 0
# suma1 = 0
# for x in range(a,b+1, 1):
#     if x % 2 == 0:
#         suma = suma + x
# print(suma)

# x = a
# while x <= b:
#     if x % 2 ==0:
#         suma1 = suma1 +x
#     x += 1

# print(suma1)


# se citeste n un nr natural urmat de n numere pe linii diferite

n = int(input("n ="))
numar_n = 0
produs = 1
while n > 0:
    numar_n = int(input("introdu numarul:"))
    produs = produs * numar_n
    n -=1

print(produs)