#iç içe while-for ile faktöriyel bulma.

sayi=int(input('Faktoriyelini istediginiz sayiyi giriniz::'))

while sayi>0:
    carpim=1
    for carpan in range(2,sayi+1):
        carpim*=carpan
    print(sayi,'!=',carpim,sep='')
    sayi=int(input('Devam etmek icin yeni bir sayi giriniz::'))
else:
    if sayi==0:
        print(sayi,'!=',1,sep='')
    else:
        print('Hatali Giris!!!')

end=input()

