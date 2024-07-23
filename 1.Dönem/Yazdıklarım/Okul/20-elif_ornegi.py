#bu program girilen 3 farklı sayının
#en büyüğünü bulur.

sayi1=int(input('sayi1::'))
sayi2=int(input('sayi2::'))
sayi3=int(input('sayi3::'))

if sayi1>sayi2>sayi3:
    print('sayi1 en buyuk')
elif sayi2>sayi3:
    print('sayi2 en buyuk')
elif sayi3>sayi2:
    print('sayi3 en buyuk')
else:
    print('esit sayilar girdin veya hatali giris yaptin.')

end=input()