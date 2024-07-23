def kuvvet(taban,us):
    if us==0:
        return 1
    else:
        return taban*kuvvet(taban,us-1)     #Burada 'us' 0'a giderken fonksiyonu sonlandırıyor.


def can():
    print('Hello can')