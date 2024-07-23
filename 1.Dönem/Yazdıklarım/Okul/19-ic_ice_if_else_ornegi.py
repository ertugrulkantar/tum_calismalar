#girilen iki sayı arasındaki ilişkiyi bulur.
#iç içe if-else yapısına örnek.

sayi1=int(input('1.sayi'))
sayi2=int(input('2.sayi'))

if sayi1>sayi2:
    print('sayi1 buyuk')
else:
    if sayi2>sayi1:
        print('sayi2 buyuk')
    else:
        print('sayilar esit')
