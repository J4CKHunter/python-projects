liste=[1,2,3]
tuple=(1,2,3)
küme={1,2,3}  #kümeler sırasızdır.içindeki elemanın ne olduğu önemlidir.1 eleman 1 kez bulunur kümede.
              # elemanın tekrarı küme için önemli değil.
print(liste)
print(tuple)
print(küme)


liste_2=[1,2,3,3,5,6,1,3,2,1]
tuple_2=(1,2,3)
küme_2={1,2,3,3,5,6,1,3,2,1,7,1,2}

print(liste_2)
print(tuple_2)
print(küme_2)

küme_3=set(liste_2)     #set içinde girilen listeyi,kümeye dönüştürür.
küme_4=set([1,2,3,1,2,3,4,55,2,1,3])

print(küme_3)
print(küme_4)


k5=set('karakartal')
k6=set('kapkaratutkal')

print(k5)
print(k6)

print(k5|k6)   #set union ---> kümelerde birleşim işlemi
print(k6-k5)   #set difference ---> kümelerde fark işlemi(k6'nın k5'ten farklı elemanları
print(k5&k6)   #set intersection ---> kümelerde kesişim işlemi
print(k6^k5)   #exclusive or ---> ( k6-k5 | k5-k6 ) veya ( (k6|k5)-k6&k5 )
