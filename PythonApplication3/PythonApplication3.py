from math import *
from, randoms import * #randint (a,b) juhuslik täisarv a ja b vahel
kommide_arv=15
print("laul on", kommide arv, "komi. " )
b=int(input("mitu komi soovitud laualt ära võtta? "))
kommide_arv =b #kommidearv vähendab b võrra 
print ("laul on nüüd", kommide arv, "kommi.")
from, randoms import * #randint (a,b) juhuslik täisarv a ja b vahel 
kommide_arv=randint (1,100) #1-100 vahel juhuslik täisarv 
try:
    vanus = int(input("Sisesta vanus: "))
    print("Järgmisel aastal oled", vanus + 1)
except ValueError:
    print("See ei olnud täisarv!")

ülesanne 4
#puu läbimõõde arvutamine 
# kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu
# ning teatab selle peale puu läbimõõdu 

ümbermõõt=float(input"sisesta puu ümbermõõt: ")

läbimõõt=ümbermõõt/pi 
print("puu läbimõõt on:" läbimõõt)

ülesanne 5
#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
n = float(input("sisesta maatüki  pikkus (n): "))
m = float (input("sisesta maatüki laius (M): "))
diagonaal = sqrt(n**2 + m**2) #** astendamine 
print("ristkülikukujulise maatüki diagonaal on:", round (diagonaal ,2))
#round()ümardab kahe kümnedkohani

#ülesanne 6
Leidke järgnevast näiteprogrammist loogiline viga:
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

#ülesanne 7
#Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
#Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, täisarvuline osa ja jääk.
arv1=int(input("sisesta esimene täisarv: "))
arv2=int(input("sisesta teine täisarv"))
arv3=int(input("sisesta kolmas täisarv"))
arv4=int(input("sisesta neljas täisarv"))
arv5=int(input("sisesta viies täisarv"))
summa=arv1+arv2+arv3+arv4+arv5
jagaja=int(input("sisesta arv, millega jagada: "))
tulemus=summa/jagaja 
print("tulemus:", tulemus)
print("täisarvuline osa:", int(tulemus))
print("jääk:", tulemus-int(tulemus))
#int(3.75)=3 teine variant täisosa leidmiseks on kasutada //jaganist
print ("jääk:",summa % jagaja)

ülesanne 8
print("@..@
 print(----)
 print( \__/ )
print^^ "" ^^  ")  

ülesanne 9
a=float(input("sisesta a täisarvz "))
b=float(input("sisesta b täisarv "))
c=float(input("sisesta c täisarv "))
print("kolmnurga ümbermõõdu pn ", P)

ülesanne 10
Võtsite sõpradega (näiteks P inimest) suure pitsa, mille hind on 12,90 €.
Jätate teenindajale 10% jootraha.
Koosta programm, mis arvutab, kui palju igaüks peab maksma.

hidn=20 
jootraha=hind * 0.10
kokku=hind + jootraha
inimese_kohta= kokku / p 
