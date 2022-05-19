liste=[1,2,3]
tuple=(1,2,3)

print(liste)
print(tuple)

liste[1]=9
# tuple[1]=9 diye bir atama yok.tuple constant bir şey olduğu için tekrar atama kabul etmez.
print(liste)

x,y,z=tuple # tuple içindeki değişkenleri sırasıyla x,y,z 'ye kopyala.
print(x,y,z)

x=15
y=197
z=100
print(x,y,z)
print(tuple)

tuple=(x,y,z) #burada yeni bir tuple tanımlaması yapılır.
print(tuple)

tuple_2=([1,2,3],[9,8,7])
print(tuple_2)

tuple_2[0][1]=100 #burada tuple içindeki elemanın elemanına eriştiğimiz için değiştirebiliriz.
                  #tuple elamanını [1,2,3] direkt değiştiremeyiz.bu eleman liste cinsinde.tuple değil.
                  #içindekini değiştirebiliriz.
print(tuple_2)