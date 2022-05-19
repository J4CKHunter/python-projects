def toplama(a,b):
    return a+b

print(toplama(2,3))
#print(toplama(3)) ==>> ben 2 değer istiyorum sen 1 verdin diğer değer kayıp diyor
#print(toplama(2,3,4)) ==>> ben 2 değer istiyorum sen 3 verdin olmaz diyor


def yazdir(*a):
    print(a)

yazdir(2,3,4,"erdem")

def yazdir2(x,y,*a):
    print(x,y,a)

yazdir2(2,3,4,5,"erdem")

