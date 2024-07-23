#Üs alma programı,for örneği.

sayi=int(input('Sayiyi giriniz::'))
us=int(input('Ussu giriniz::'))
carpim=1  #İlk değer oluşturmak için.Çarpmada 1,toplamada 0 alınır.

for kuvvet in range(us):
    print('Sayının',kuvvet,'.kuvveti=',carpim)
    carpim=sayi*carpim
print('Sonuc',kuvvet+1,'.kuvveti=',carpim)

end=input()