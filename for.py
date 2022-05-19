liste1=[1,3,5,7,9,15]
toplam1=0
for i in liste1:
    toplam1=toplam1+i
    print(i)

print(toplam1)


toplam2=0
for j in liste1[2:4]:
    toplam2=toplam2+j
    print(j)

print(toplam2)

for x in range(5):
    print(x)
print("\n")

for a in range(1,5):
    print(a)
print("\n")

for b in range(1,5,+2):
    print(b)
print("\n")

for c in range(100,50,-10):
    print(c)
print("\n")

for d in liste1[:2]:
    print(d)
print("\n")

for e in liste1[2:5]:
    print(e)
print("\n")

for w in range(1,21):
    if w%3!=0:
        print(w)
print("\n")

for n in range(1,21,+2):
    if n%3!=0:
        print(n)
print("\n")

for o in range(21,1,-1):
    if o%2!=0:
        print(o)