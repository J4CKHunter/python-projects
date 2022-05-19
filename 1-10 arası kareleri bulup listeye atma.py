liste=[]

for i in range(1,11):
    liste.append((i)**2)

#for i in range(10):
#   liste.append((i+1)**2)

print(liste)
print(i) # NORMALDE FOR İÇİNDE TANIMLANANLAR FOR İÇİNDE KALIR C'DE.
         # AMA PYTHON'DA side effect OLARAK FOR.UN DIŞINDA DA TANIMLI OLUYOR.


         #BU side effecti ORTADAN KALDIRMAK İÇİN BÖYLE BİR GEÇİCİ LAMBDA FONKSİYONU TANIMLIYORUZ.

liste_2=list(map(lambda x:x**2,range(1,11)))

print(liste_2)


        #VEYA BÖYLE BİR FONKSİYON KULLANABİLİRİZ.
liste_3=[x**2 for x in range(1,11)] # x'in karesini al , x'in 1-11 arası alacagı degerler için,normal ingilizce cümle.
print(liste_3)
