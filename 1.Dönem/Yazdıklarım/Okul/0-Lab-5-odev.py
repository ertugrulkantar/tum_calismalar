takim_mac_sayisi=int(input('Takimin sezon boyu oynadiği mac sayisini giriniz::'))

en_skorer_oyuncunun_mactaki_skoru=0
takimin_sezondaki_toplam_skoru=0
oyuncu_sayaci=0
takimin_yuzden_fazla_skor_urettigi_maclar=0
takimin_skor_rekoru=0
bu_mac_icin_oyuncu_sayaci=0


while takim_mac_sayisi<=0:
    print('Hatali Giris!!!')
    takim_mac_sayisi=int(input('Mac sayisini yeniden giriniz::'))

for sayac in range(0,takim_mac_sayisi):
    print(sayac+1,end='')
    macin_tarihi=input('.mac tarihini giriniz::')
    takimin_o_mactaki_toplam_sayisi = 0
    oyuncu_dongu_degiskeni = 'e'       #while giriş için başlangıç.
    en_skorer_oyuncunun_mactaki_skoru=0     #sıradaki maç için sıfırlama
    en_skorer_oyuncu=0    #sıradaki maç için sıfırlama

    while oyuncu_dongu_degiskeni=='e' or oyuncu_dongu_degiskeni=='E':
        oyuncu_sayaci+=1
        bu_mac_icin_oyuncu_sayaci+=1
        print(bu_mac_icin_oyuncu_sayaci,end='')
        oyuncu_ad_soyad=input('. oyuncunun ad-soyadini giriniz::')
        bireysel_skor=int(input('Oyuncunun mactaki skorunu giriniz::'))

        while bireysel_skor<0:
            print('Oyuncunun skorunu hatali girdiniz!!!')
            bireysel_skor=int(input('Oyuncunun mactaki skorunu yeniden giriniz::'))

        takimin_o_mactaki_toplam_sayisi += bireysel_skor

        if takimin_o_mactaki_toplam_sayisi>100:
            takimin_yuzden_fazla_skor_urettigi_maclar+=1

        if takimin_skor_rekoru<takimin_o_mactaki_toplam_sayisi:
            rekor_tarihi=macin_tarihi
            takimin_skor_rekoru=takimin_o_mactaki_toplam_sayisi


        if en_skorer_oyuncunun_mactaki_skoru<bireysel_skor:
            en_skorer_oyuncu=str(oyuncu_ad_soyad)
            en_skorer_oyuncunun_mactaki_skoru=bireysel_skor

        print('Baska oyuncu girmek ister misiniz?')
        oyuncu_dongu_degiskeni=input('(E/e/H/h)::')

        while oyuncu_dongu_degiskeni!='E' and oyuncu_dongu_degiskeni!='e' and oyuncu_dongu_degiskeni!='H' and oyuncu_dongu_degiskeni!='h':
            print('Hatali Giris!!!')
            oyuncu_dongu_degiskeni=input('Lutfen yalnizca Evet(E/e) veya Hayir(H/h) giriniz::')

    bu_mac_icin_oyuncu_sayaci=0

    takimin_sezondaki_toplam_skoru+=takimin_o_mactaki_toplam_sayisi

    print('Takimin',sayac+1,'. macta attigi toplam sayi::',takimin_o_mactaki_toplam_sayisi)
    print('Takimin',sayac+1,'. macta en skorer oyuncusu::',en_skorer_oyuncu,',bu oyuncunun mactaki skoru::',en_skorer_oyuncunun_mactaki_skoru)

print('Takimin mac basina attigi ortalama sayi::',format(takimin_sezondaki_toplam_skoru/takim_mac_sayisi,'.2f'))
print('Takimin mac basina oynayan ortalama oyuncu sayisi::',format(oyuncu_sayaci/takim_mac_sayisi,'.2f'))
print('Takimin 100 sayidan fazla skor urettigi mac sayisi::',takimin_yuzden_fazla_skor_urettigi_maclar,
      'bu maclarin tum maclar icindeki yuzdesi::%',format(takimin_yuzden_fazla_skor_urettigi_maclar*100/takim_mac_sayisi,'.2f'))
print('Takimin sayi rekorunu kirdigi tarih::',rekor_tarihi,'Bu tarihte takimin skor rekoru::',takimin_skor_rekoru)

end=input()










