print("hangi siradaki fibonacci sayisini istiyorsunuz")
x=int(input())

a=0
b=1
k=0
while k<x:

    c=a+b
    a=b
    b=c
    print(a)
    k=k+1


