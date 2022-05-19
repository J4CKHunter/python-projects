liste_1=[1,2,3,4]
liste_2=[24,63,86,37]
liste_3=[1952,945,321,801,32315]

liste_1=liste_2             ######    SHALLOW COPY    ######

print(liste_1)
print(liste_2)

liste_2.append(3000)

print(liste_1)
print(liste_2)

liste_1=liste_3.copy()      ######    HARD COPY    ######
liste_1.append(1709563)

print(liste_1)
print(liste_3)


