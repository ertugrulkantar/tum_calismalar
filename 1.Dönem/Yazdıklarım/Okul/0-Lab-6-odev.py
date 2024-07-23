import math

def sayi_al(alt_sinir,ust_sinir):
    print(alt_sinir,ust_sinir,sep='-',end='')
    print(' Aralıgında bir reel sayi giriniz::',end='')
    sayi=float(input())
    while sayi<int(alt_sinir) or sayi>int(ust_sinir):
        sayi=float(input('Hatali giris,lutfen aralikta bir sayi giriniz::'))
    return sayi




def dikdortgen_alani(kenar1_uzunlugu,kenar2_uzunlugu):
    dikdortgenin_alani=kenar1_uzunlugu*kenar2_uzunlugu
    return dikdortgenin_alani



def eskenar_ucgen_alani(kenar_uzunlugu):
    eskenar_ucgenin_alani=((kenar_uzunlugu**2)*(3**(1/2)))/4
    return eskenar_ucgenin_alani



def daire_alani(yaricap_uzunlugu):
    dairenin_alani=math.pi*(yaricap_uzunlugu**2)
    return dairenin_alani



def dikdortgen_prizma_yuzey_alani(taban1,taban2,yukseklik):
    dikdortgen_prizmanin_yuzey_alani=dikdortgen_alani(taban1,taban2)*2+dikdortgen_alani(taban1,yukseklik)*2+dikdortgen_alani(taban2,yukseklik)*2
    return dikdortgen_prizmanin_yuzey_alani



def kare_prizma_yuzey_alani(taban_kenar_uzunlugu,yukseklik):
    kare_prizmanin_yuzey_alani=dikdortgen_alani(taban_kenar_uzunlugu,taban_kenar_uzunlugu)*2+dikdortgen_alani(taban_kenar_uzunlugu,yukseklik)*4
    return kare_prizmanin_yuzey_alani



def kup_yuzey_alani(kenar_uzunlugu):
    kupun_yuzey_alani=dikdortgen_alani(kenar_uzunlugu,kenar_uzunlugu)*6
    return kupun_yuzey_alani



def eskenar_ucgen_prizma_yuzey_alani(taban_uzunlugu,yukseklik):
    eskenar_ucgen_prizmanin_yuzey_alani=(eskenar_ucgen_alani(taban_uzunlugu)*2)+dikdortgen_alani(taban_uzunlugu,yukseklik)*3
    return eskenar_ucgen_prizmanin_yuzey_alani



def ucgen_piramit_yuzey_alani(kenar_uzunlugu):
    ucgen_piramitin_yuzey_alani=eskenar_ucgen_alani(kenar_uzunlugu)*4
    return ucgen_piramitin_yuzey_alani



def silindir_yuzey_alani(taban_yaricapi,yukseklik):
    daire_cevresi=2*math.pi*taban_yaricapi
    silindirin_yuzey_alani=(daire_alani(taban_yaricapi)*2)+daire_cevresi*yukseklik
    return silindirin_yuzey_alani

print('Asagida 2-10 araliginda uc adet reel sayi giriniz.')
sayi1=sayi_al(2,10)
sayi2=sayi_al(2,10)
sayi3=sayi_al(2,10)


print('Taban kenar uzunluklari sayi1 ve sayi2 olan,yuksekligi sayi3 olan dikdortgen prizmanin yuzey alani=',end='')     #printleri iç içe yapmak yerine
print(format(dikdortgen_prizma_yuzey_alani(sayi1,sayi2,sayi3),'.2f'))                                                   #ikiye ayırdım çünkü
                                                                                                                        #karmaşıklık iç içede
print('Taban kenar uzunluklari sayi1+sayi2 olan,yuksekligi sayi3 olan kare prizmanin yuzey alani=',end='')              #bence artıyor.
print(format(kare_prizma_yuzey_alani(sayi1+sayi2,sayi3),'.2f'))

print('Kenar uzunlugu sayi1+sayi2+sayi3 olan kupun yuzey alani=',end='')
print(format(kup_yuzey_alani(sayi1+sayi2+sayi3),'.2f'))

print('Taban kenar uzunluklari sayi1+sayi2 olan,yuksekligi sayi3 olan eskenar ucgen prizmanin yuzey alani=',end='')
print(format(eskenar_ucgen_prizma_yuzey_alani(sayi1+sayi2,sayi3),'.2f'))

print('Kenar uzunlugu sayi1+sayi2+sayi3 olan ucgen piramidin yuzey alani=',end='')
print(format(ucgen_piramit_yuzey_alani(sayi1+sayi2+sayi3),'.2f'))

print('Taban yaricapi uzunlugu sayi1+sayi2 olan,yuksekligi sayi3 olan silindirin yuzey alani=',end='')
print(format(silindir_yuzey_alani(sayi1+sayi2,sayi3),'.2f'))

end=input()







