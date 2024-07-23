#bu program iki sayıyı küçükten büyüğe sıralar.

sayi1=float(input('1.sayiyi giriniz::'))
sayi2=float(input('2.sayiyi giriniz::'))

if sayi1>sayi2:
    print('kucuk sayi=',sayi2,'buyuk sayi=',sayi1)

if sayi2>sayi1:
    print('kucuk sayi=',sayi1,'buyuk sayi=',sayi2)

if sayi2==sayi1:
    print('sayilar esit')

print(type(sayi1)) #Eğer baştaki 'float'ları silersen sayı olarak değil
                   #str olarak karşılaştırır.
end=input()
