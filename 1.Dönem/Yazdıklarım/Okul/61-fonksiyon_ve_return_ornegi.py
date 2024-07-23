def uc_sayinin_en_buyugu(sayi1,sayi2,sayi3):
    max_sayi=0
    if sayi1>sayi2>sayi3:
        max_sayi=sayi1
    elif sayi2>sayi3:
        max_sayi=sayi2
    else:
        max_sayi=sayi3
    return max_sayi     #return ne işe yarar?Değer döndürür ve o değeri istediğin
                        #yerde kullanabilirsin.

s1=int(input('Birinci sayiyi giriniz::'))
s2=int(input('İkinci sayiyi giriniz::'))
s3=int(input('Ucuncu sayiyi giriniz::'))

print('En buyuk sayi:',uc_sayinin_en_buyugu(s1,s2,s3))

end=input()
