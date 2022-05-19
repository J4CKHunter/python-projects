print("hangi siradaki fibonacci sayisini istiyorsunuz")
x=int(input())

a=0
b=1
k=0
while k<x:

    a,b=b,a+b
    print(a)
    k=k+1
