f=open('bilgisayar.txt','w')
f.write('erdem nayin\nkerem nayin\nsebile nayin\nbilal nayin')
f.close()

f=open('bilgisayar.txt','w')
print(f.write('erdem nayin\nkerem nayin\nsebile nayin\nbilal nayin'))#kaç karakterden oluştuğunu sayar.
f.close()

f=open('bilgisayar.txt','r')
print(f.readline())
f.close()

#>>> f.readline() dosyadan 1 satır okur ve sonuna \n koyar.
#'This is the first line of the file.\n'
#>>> f.readline()
#'Second line of the file\n'
#>>> f.readline()

f=open('bilgisayar.txt','r') #eğer tüm satırları yazdırmak istiyorsak
for line in f:
    print(line,end='')     #sona '' koymak bişey koymamaktır.
f.close()



print('\n')



f=open('bilgisayar.txt','r')
print(list(f))                      #her satırı liste olarak okumak istiyorsak.
f.close()

f=open('bilgisayar.txt','r')
print(f.readlines())                #her satırı liste olarak okumak istiyorsak.
f.close()

# f.tell() imleçin yerini integer değer olarak döndürür.
# f.seek(koyulacağı yer,nereden başlaycak)

#               nereden başlayacak=0  -->  dosyanın başından
#               nereden başlayacak=1  -->  imlecin şu anki konumundan
#               nereden başlayacak=2  -->  dosyanın sonundan

