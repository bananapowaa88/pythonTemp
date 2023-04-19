## PROG TÉTELEK ##
# 1. feladat
"""
Generálj 10 darab véletlenszámot [-5;5] intervallumban, és tedd be őket egy listába.
Írasd ki a számokat, az összegüket és az átlagukat!
"""
print("-----Prog. tétel: 1. feladat-----")
import random

lista = []

for i in range(10):
    lista.append(random.randint(-5,5))

print(f"A lista: {lista}")
# Átlag
lista_osszeg = 0
for elem in lista:
    lista_osszeg += elem

print(f"A lista összege: {lista_osszeg}")
print(f"A lista átlaga: {lista_osszeg/len(lista)}")

# 2. feladat
"""
Csak a pozitív számokat összegezd!
"""
print("-----Prog. tétel: 2. feladat-----")

lista_poz_osszeg = 0
for elem in lista:
    if elem > 0:
        lista_poz_osszeg += elem

print(f"A lista pozitív elemei: {lista_poz_osszeg}")

# 3. feladat
"""
Kérj be érdemjegyeket, töltsd őket egy listába!
Az adatbevitel akkor fejeződjön be, amikor az [1;5] intervallumon kívüli érték érkezik.
Számold ki a jegyek átlagát!
"""
print("-----Prog. tétel: 3. feladat-----")

erdemjegyek = []
jegy = int(input("Érdemjegy: "))
while jegy >= 1 and jegy <= 5:
    erdemjegyek.append(jegy)
    jegy = int(input("Érdemjegy: "))
print(erdemjegyek)
if len(erdemjegyek) != 0:
    jegy_osszeg = 0
    for j in erdemjegyek:
        jegy_osszeg += j
    print(f"A jegyek átlaga: {jegy_osszeg/len(erdemjegyek)}")

# 4. feladat
"""
Számítsd ki a felhasználó által megadott szám faktoriálisát!
(pl. 4!=1*2*3*4; 0!=1;	1!=1)
"""
print("-----Prog. tétel: 4. feladat-----")

szam = int(input("Minek a faktoriálisát számoljam ki?"))

faktorialis = 1
if szam != 0:
    while szam > 1:
        faktorialis *= szam
        szam -= 1
else:
    faktorialis = 1
print(f"A szám faktoriálisa: {faktorialis}")

# 5. feladat
"""
Generálj 10 véletlenszámot a [0;100] intervallumban, és tedd őket egy listába.
Hány olyan szám van a listában, amely osztható 5-tel, de nem osztható 25-tel?
"""
print("-----Prog. tétel: 5. feladat-----")

import random
lista = []
darabszam = 0
for i in range(10):
    lista.append(random.randint(0, 100))
    elem = lista[i]
    if elem % 5 == 0 and elem % 25 != 0:
        darabszam += 1
print(f"5-tel osztható, 25-el nem osztható számok száma: {darabszam}")


# 6. feladat
"""
Generálj 10 véletlenszámot [0;10] intervallumban, és  tedd őket egy listába.
Hány olyan szám van, ami egyenlő a szomszédai átlagával?
"""
print("-----Prog. tétel: 6. feladat-----")

import random
lista = []

for i in range(10):
    lista.append(random.randint(0, 10))

print(lista)
egyenlo_szomszed_darab = 0
i = 0
while i < len(lista):
    # A 0. elemnek a következő elem a szomszédja
    if i == 0:
        if lista[i] == lista[i+1]:
            egyenlo_szomszed_darab += 1
            print(lista[i])
    # Az utolsó elemnek az előző elem a szomszédja
    if i == len(lista)-1:
        if lista[i] == lista[i-1]:
            egyenlo_szomszed_darab += 1
            print(lista[i])
    # A többi elemnél kiszámoljuk az átlagot
    if i > 0 and i != len(lista)-1:
        osszeg = lista[i-1] + lista[i+1]
        if lista[i] == osszeg / 2:
            egyenlo_szomszed_darab += 1
            print(lista[i])
    i += 1
print(f"A keresett elemek száma: {egyenlo_szomszed_darab}")

# 7. feladat
"""
Tölts fel egy 6 elemű listát tetszőleges szövegekkel!
Hány olyan szöveg van a listában, amely tartalmazza az „e” betűt?
Írasd is ki ezeket a képernyőre!
"""
print("-----Prog. tétel: 7. feladat-----")

lista = ["alma", "körte", "szilva", "szőlő", "dió", "avokádó"]

e_darab = 0
for i in lista:
    if "e" in i:
        e_darab += 1
print(f"\'e\' betűt tartalmazó szövegek száma a listában: {e_darab}")

# 8. feladat

"""
Hány „a” betűvel kezdődő szöveg van a fenti listában?
"""

print("-----Prog. tétel: 8. feladat-----")

lista = ["alma", "körte", "szilva", "szőlő", "dió", "avokádó"]

a_kezdodo = 0
for i in lista:
    if i.startswith("a"):
        a_kezdodo += 1
print(f"\'a\' betűvel keződő szövegek száma a listában: {a_kezdodo}")

# 9. feladat
"""
Hőmérséklet értékekkel töltünk fel egy listát [-15;20] között. Mekkora a legnagyobb hőingadozás mértéke?
"""
print("-----Prog. tétel: 9. feladat-----")

import random

homersekletek = []

for i in range(20):
    homersekletek.append(random.uniform(-15,20))

print(homersekletek)
legnagy_hoing = 0
for i in range(1, len(homersekletek)):
    diff = abs(homersekletek[i-1] - homersekletek[i])
    if legnagy_hoing < diff:
        legnagy_hoing = diff

print(f"A legnagyobb hőingadozás: {legnagy_hoing}")

# 10. feladat
"""
Határozd meg a listában a legenyhébb fagypont alatti hőmérsékletet!
"""
print("-----Prog. tétel: 10. feladat-----")

# Megkeressük, hogy van-e negatív érték
van_neg = False
for i in homersekletek:
    if i < 0:
        van_neg = True
        enyh_fagyp_alatti = i

if van_neg:
    for i in homersekletek:
        # Ha negatív az érték és az eddigi maxtól nagyobb
        if i < 0 and enyh_fagyp_alatti < i:
            enyh_fagyp_alatti = i

    print(f"Fagypont alatti legenyhébb hőmérséklet: {enyh_fagyp_alatti}")
else:
    print("Nincs fagypont alatti hőmérséklet.")


# 11. feladat
"""
Tölts fel egy 25 elemű tömböt véletlenszámokkal [1;10] között.
Melyik szám szerepel benne legtöbbször egymás mellett?
"""
print("-----Prog. tétel: 11. feladat-----")

### String gyakorlásban előfordult feladat

# 12. feladat
"""
Egy 10 elemű listában, melyet véletlenszámokkal töltünk fel [0;10] között, döntsük el, hogy van-e olyan elem, mely az őt megelőző elem duplája!
"""
print("-----Prog. tétel: 12. feladat-----")

import random

lista = []

for i in range(10):
    lista.append(random.randint(0,10))

print(lista)
van = False

for i in range(1, len(lista)-1):
    if lista[i-1] * 2 == lista[i]:
        print(lista[i])
        van = True

if van:
    print("Van olyan elem, amely a duplája, mint az őt megelőző elem.")
else:
    print("Nincs olyan elem, amely duplája, mint az előző elem.")

# 13. feladat
"""
Kockával dobunk 20-szor. Az értékeket tegyük egy listába. Volt-e olyan, hogy kétszer egymás után 6-ost dobtunk?
"""
print("-----Prog. tétel: 13. feladat-----")

import random

lista = []

for i in range(20):
    lista.append(random.randint(1,6))

print(lista)

van = False
for i in range(1, len(lista)-1):
    if lista[i-1] == lista[i] and lista[i] == 6:
        van = True
if van:
    print("Van 2 darab 6-os egymás mellett.")
else:
    print("Sajnos nincs 2 darab 6-os egymás mellett.")

# 14. feladat
"""
Egy útvonal adatait listában tároljuk.
A szárazföldet 1-es, a tócsát 0-val jelezzük.
Olvassuk be az útvonal hosszát, majd az adott méretű listában generáljunk véletlenszerűen 1-eseket és 0-kat.
Át tudunk-e jutni ezen az útvonalon, ha tudjuk, hogy maximum 3 tócsát tudunk átugrani?
"""
print("-----Prog. tétel: 14. feladat-----")

import random

utvonal = []

hossz = int(input("Add meg az útvonal hosszát: "))
for i in range(hossz):
    utvonal.append(random.randint(0,1))

print(utvonal)
tocsak_szama = 0
for i in utvonal:
    if i == 0:
        tocsak_szama += 1
if tocsak_szama <= 3:
    print(f"Siker! A tócsák száma: {tocsak_szama}")
else:
    print(f"Sajnos nem sikerült. A tócsák száma: {tocsak_szama}")
