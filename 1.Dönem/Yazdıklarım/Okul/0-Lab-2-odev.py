oyuncu_adi=input('oyuncu adini giriniz::')
oyun_turu=input('oyun FIBA kurallarına gore mi NBA kurallarına gore mi oynaniyor?'
                'Girdi yalnizca FIBA veya NBA olmalidir::')

if oyun_turu=='FIBA' :    #burada else kullanmamamın sebebi girdi seçeneklerini başta belirtmem.
    faul_siniri=5         #ve saçma girdi olursa error alınması için.
if oyun_turu=='NBA' :
    faul_siniri=6

oyuncunun_attigi_toplam_sayi=int(input('oyuncunun toplam skoru::'))
oyuncunun_toplam_ribaundu=int(input('oyuncunun toplam ribaundu::'))
oyuncunun_toplam_asisti=int(input('oyuncunun toplam asisti::'))
oyuncunun_toplam_top_calma_sayisi=int(input('oyuncunun toplam top calma sayisi::'))
oyuncunun_toplam_blok_sayisi=int(input('oyuncunun toplam blok sayisi::'))
oyuncunun_solo_faul_sayisi=int(input('oyuncunun solo faul sayisi::'))

if oyuncunun_attigi_toplam_sayi>=10:
    oyuncu_performansi=1                 #burada else kullanmamın sebebi daha sonra tekrar
else:                                    #kullanacağım oyuncu_performansi değişkeninin
    oyuncu_performansi=0                 #if Clause False olsa dahi tanımlı olması içindir.

if oyuncunun_toplam_ribaundu>=10:
    oyuncu_performansi=oyuncu_performansi+1

if oyuncunun_toplam_asisti>=10:
    oyuncu_performansi=oyuncu_performansi+1

if oyuncunun_toplam_top_calma_sayisi>=10:
    oyuncu_performansi=oyuncu_performansi+1

if oyuncunun_toplam_blok_sayisi>=10:
    oyuncu_performansi=oyuncu_performansi+1

print('Sayin',oyuncu_adi,':')

if oyuncu_performansi>=3:
    print(''''Triple Double' yaptin!!''')
else:
    print('Pek parlak değilsin...')

if oyuncunun_solo_faul_sayisi>=faul_siniri :
    print('Cok faullu oynadin. Centilmen değilsin.')
else:
    print('Bravo, Centilmensin!')

end=input('end')