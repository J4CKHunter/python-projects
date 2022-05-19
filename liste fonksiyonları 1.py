liste=[1,2,3,4]
print(liste)

print(len(liste)) #LİSTENİN ELEMAN SAYISINI SÖYLER.

liste.append(5) #SONA İSTEDENİLENİ EKLER.
liste.append("erdem")
print(liste)

liste.insert(2,9) #BELİRTİLEN SİRAYA İSTENİLENİ EKLER.
print(liste)

liste.append(9)
print(liste)

liste.remove(9) #VERDİGİMİZ DEGERİ LİSTEDE İLK KARSİLASTIGI ANDA SİLER.YANİ 2 TANE VARSA 1.SİNİ SİLER.
print(liste)

liste.remove(9)
print(liste)

print(liste.pop(3)) #LİSTENİN İSTENİLEN YERİNDEKİ DEGERİ ALIR VE LİSTEDEN KALDIRIR VE KENDİNE RETURN EDER.
print(liste)

print(liste.index("erdem")) #GİRİLEN DEGERİN LİSTEDEKİ YERİNİ BULUR VE SÖYLER.

liste.append(2)
liste.insert(0,2)

print(liste)
print(liste.count(2)) #GİRİLEN DEĞERİN LİSTEDEKİ SAYISINI SÖYLER.

liste2=[17,95,63,0]
liste.extend(liste2) #VERİLEN LİSTEYİ ASIL LİSTEMİZİN SONUNA EKLER.
print(liste)

liste.append(liste2) #VERİLEN LİSTEYİ APPEND FONKKSİYONU TEK ELEMAN OLARAK EKLER.YANİ ALT LİSTE(ALT KÜME).
print(liste)

liste2.sort()   #LİSTEYİ SIRALAR.EGER LİSTEDE STRİNG VARSA SIRALAYAMAZ.HARF İLE SAYI NASIL SIRALANSIN.
                #'<' not supported between instances of 'str' and 'int'
print(liste2)

liste.clear() #LİSTEYİ SIFIRLAR,TÜM ELEMANLARI SİLER.
print(liste)

liste2[:]     #LİSTEYİ SIFIRLAR,TÜM ELEMANLARI SİLER.
print(liste)

liste5=[1,2,3,4,5,6,7,8,9]
print(liste5)

liste5.reverse()   #LİSTEYİ TERS ÇEVİRİR.
print(liste5)

