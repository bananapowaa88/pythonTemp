# 3. feladat - Sebességek

import random

sebessegek = []

for i in range(30):
    sebessegek.append(random.randint(50, 150))
print("Sebességek: ", sebessegek)

# Átlag
osszeg = 0
for i in sebessegek:
    osszeg += i

atlag = osszeg / len(sebessegek)
print("Átlag: ", atlag)

# Terjedelem
min = 150
max = 0

for i in sebessegek:
    if i > max:
        max = i

for i in sebessegek:
    if i < min:
        min = i

print("Min érték: ",min)
print("Max érték: ", max)
terjedelem = max - min
print("Terjedelem: ", terjedelem)

kert_seb = int(input("Add meg a sebességet: "))
darab = 0
if kert_seb in sebessegek:
    for i in sebessegek:
        if i == kert_seb:
            darab += 1

print("A kért sebesség ennyiszer szerepel: ", darab)

gyorshajtas = 0
korlat = 60 * 1.1
print(korlat)

for i in sebessegek:
    if i >= korlat:
        gyorshajtas += 1

print("Gyorshajtások száma: ", gyorshajtas)