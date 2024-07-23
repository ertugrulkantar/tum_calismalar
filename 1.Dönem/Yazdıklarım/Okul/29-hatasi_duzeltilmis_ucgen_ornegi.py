kenar1=int(input('Birinci kenar:'))
kenar2=int(input('İkinci kenar:'))
kenar3=int(input('Ucuncu kenar:'))





if kenar1>kenar2 and kenar1>kenar3:  #Burada kenar1>kenar2>kenar3 yazıyordu ki bir 
    en_uzun_kenar=kenar1             #sebep oluyor.
    diger_kenarlar_toplami=kenar2+kenar3
    diger_kenarlar_kareleri_toplami=kenar2**2+kenar3**2  
elif kenar2>kenar3:
    en_uzun_kenar=kenar2
    diger_kenarlar_toplami=kenar1+kenar3
    diger_kenarlar_kareleri_toplami=kenar1**2+kenar3**2   
else:
    en_uzun_kenar=kenar3
    diger_kenarlar_toplami=kenar1+kenar2
    diger_kenarlar_kareleri_toplami=kenar1**2+kenar2**2    


if en_uzun_kenar>diger_kenarlar_toplami:
    print('Bu ucgen olamaz')
elif (en_uzun_kenar)**2==diger_kenarlar_kareleri_toplami:
    print('Dik ucgen')
elif (en_uzun_kenar)**2>diger_kenarlar_kareleri_toplami:
    print('Genis ucgen')
else:
    print('Dar ucgen')

end=input()



