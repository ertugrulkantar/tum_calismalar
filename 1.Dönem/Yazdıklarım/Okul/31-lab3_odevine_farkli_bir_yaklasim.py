oyuncu_numarasi=int(input('Oyuncu numarasi::'))
if oyuncu_numarasi!=1 and oyuncu_numarasi!=2 and oyuncu_numarasi!=3 and oyuncu_numarasi!=4 and oyuncu_numarasi!=5 :
    print('Hatali giris')
else:
    normal_sezon_mac_sayisi=int(input('Normal sezon mac sayisi::'))
    normal_sezon_sayi=int(input('Normal sezon sayi::'))
    normal_sezon_asist=int(input('Normal sezon asist::'))
    normal_sezon_ribaund=int(input('Normal sezon ribaund'))

    playoff=input('''Oyuncu takimi playoff'ta mi (E/H)::''')
    if playoff=='E':
        normal_sezon_mac_sayisi=normal_sezon_mac_sayisi+int(input('Playoff mac sayisini giriniz::'))  #toplamlı değişken yapmak
        normal_sezon_sayi=normal_sezon_sayi+int(input('Playoff sayi giriniz::'))                      #yerine tek değişkende
        normal_sezon_asist=normal_sezon_asist+int(input('Playoff asist sayisini giriniz::'))          #topladım.
        normal_sezon_ribaund=normal_sezon_ribaund+int(input('Playoff ribaund sayisini giriniz'))

    ortalama_sayi=round(normal_sezon_sayi/normal_sezon_mac_sayisi,2)
    ortalama_asist=round(normal_sezon_asist/normal_sezon_mac_sayisi,2)
    ortalama_ribaund=round(normal_sezon_ribaund/normal_sezon_mac_sayisi,2)

    print('Toplam mac sayisi::',normal_sezon_mac_sayisi)
    print('Ortalama sayi::',ortalama_sayi)
    print('Ortalama asist::',ortalama_asist)
    print('Ortalama ribaund::',ortalama_ribaund)

end=input()



