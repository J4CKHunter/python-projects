def f(x):
    return x+10
def merhaba():
    print("merhaba")
    return 0
def merrhaba():
    return print("merhaba")

print(f(int(input("sayi giriniz"))))
print(f(15))
merhaba()
print(merhaba())
merrhaba()

def fact(i):
    sonuc=1
    a=1
    while a<=i:
        sonuc = sonuc * a
        a = a + 1

    return sonuc

print(fact(5))

def faktoriyel(j):
    if(j<0):
        return "FALSE"
    elif (j == 0):
        return 1

    return j * faktoriyel(j-1)

print("sonuc "+str(faktoriyel(5)))
print(faktoriyel(int(input("istediginiz faktoriyeli girin"))))

def fibo(o):
    if(o == 0):
        return 0
    if(o == 1):
        return 1
    return fibo(o-1)+fibo(o-2)

print(fibo(int(input("istediginiz siradaki fibonacci sayisini girin:"))))

def fonk2(x,y):
    return x+10+5*y

print(fonk2(2,3))

def fonk3(x,y=3):
    return x+2*y

print(fonk3(2,5))
print(fonk3(2))
