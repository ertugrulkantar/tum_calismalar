def sayi_al(alt_sinir,ust_sinir):
    sayi=int(input('Sayiyi giriniz::'))
    while sayi<alt_sinir or sayi>ust_sinir:
        sayi=int(input('Hatali veri girisi,lutfen tekrar giriniz::'))
    return sayi

secim=sayi_al(1,10)
print(secim,'dogru secim',sep=',')

def dikdortgen_ciz(dikey_kenar,yatay_kenar):
    for i in range(dikey_kenar):
        for j in range(yatay_kenar):
            print('*',end='')  #burda boşluk var
        print(' ')              #burda yok!!

dikey_kenar=int(input('Dikdortgenin dikey kenarini giriniz::'))
yatay_kenar=int(input('Dikdortgenin yatay kenarini giriniz::'))
dikdortgen_ciz(dikey_kenar,yatay_kenar)


def faktoriyel(sayi):
    carpim=1
    for carpan in range(1,sayi+1):
        carpim*=carpan
    return carpim

faktoriyel_sayi=int(input('Hangi sayinin faktoriyeli bulunsun::'))
print(faktoriyel(faktoriyel_sayi))

def kombinasyon(n,k):
    return(faktoriyel(n)/(faktoriyel(k)*faktoriyel(n-k)))

print(kombinasyon(5,3))


def menu_goruntule(a,b):
    print('Dikdortgen cizmek icin 1')
    print('Faktoriyel hesaplama icin 2')
    print('Kombinasyon hesaplama icin 3')
    print('Cikis icin 0')
    tercih=int(input())
    if tercih==1:
        dikdortgen_ciz(5,3)
    if tercih==2:
        faktoriyel(8)
    if tercih==3:
        kombinasyon(6,2)
    if tercih==0:
        print('Hoscakal!!!')
    if not(a<=tercih<=b):
        print('HATA')

menu_goruntule(1,3)
