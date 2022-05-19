kontrol=0
for i in range(2,101):
    kontrol=0
    for j in range(2,i):
        if i % j == 0:
            kontrol=1
            break
    if kontrol==0:
        print(i)