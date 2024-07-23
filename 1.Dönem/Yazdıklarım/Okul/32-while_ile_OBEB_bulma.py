#Bu program OBEB hesaplar.
#Yöntemi:
#Büyük olan sayıyı bölünen,küçük olan sayıyı bölen olarak ata.
#Daha sonra ilk böleni bölünen olarak al ve ilk işlemin kalanına böl.Kalan olarak sıfır yakalayana dek
#devam et.
#Sıfırı bulduğun işlemdeki bölen bu iki sayının OBEB'idir.

sayi1=int(input('Birinci sayiyi giriniz::'))
sayi2=int(input('İkinci sayiyi giriniz::'))

if sayi1>sayi2:
    bolunen=sayi1
    bolen=sayi2
else:
    bolunen=sayi2
    bolen=sayi1

kalan=bolunen%bolen

while kalan!=0:
    bolunen=bolen
    bolen=kalan
    kalan=bolunen%bolen

print('Bu iki sayinin obebi',bolen,sep='=')

end=input()