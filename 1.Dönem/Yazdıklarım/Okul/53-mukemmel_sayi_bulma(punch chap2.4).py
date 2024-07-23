#Mükemmel sayı bulma.
#Punch'n Enbody Slayt-2.4 örneği.

bolenlerin_toplami=0
sayi=int(input('Sayiyi giriniz::'))

while sayi>0:
    bolenlerin_toplami=0
    for bolen in range(1,sayi):
        if sayi%bolen==0:
            bolenlerin_toplami+=bolen

    if bolenlerin_toplami==sayi:
        print(sayi,' Sayisi Mukemmel!!!',sep='')
    else:
        print(sayi,' sayisi mukemmel degil',sep='')

    sayi=int(input('Devam icin yeni bir sayi giriniz::'))

end=input

