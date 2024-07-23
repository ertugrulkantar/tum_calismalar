def sayi_al(alt_sinir,ust_sinir):
    hata_var_mi=True
    while hata_var_mi==True:
        try:
            sayi=int(input('::'))
            if ust_sinir=='*':      #Üst sınırı olmayan değerlerin döngüye uyması için.Kodu kısaltmaya çalıştım.
                ust_sinir=sayi+1
            while sayi<alt_sinir or sayi>ust_sinir:
                sayi=int(input('Girisiniz sinir degerlerine uymuyor.Lutfen tekrar giris yapiniz::'))
            hata_var_mi=False
        except ValueError:
            print('Deger hatasi,lutfen tekrar giriniz')
            hata_var_mi=True
        except:
            print('Hata,lutfen tekrar giriniz')
            hata_var_mi=True
    return sayi

def main():


    oyuncu_skor_dict={}

    print('Takimin toplam mac sayisini giriniz')
    takimin_toplam_mac_sayisi=sayi_al(1,'*')    #Üst sınır değeri yok,yukarıda açıklamıştım.

    mevki_skor_iki_boyutlu_listesi=[]
    for satir in range(takimin_toplam_mac_sayisi):
        mevki_skor_iki_boyutlu_listesi.append([0]*5)    #Sütun sayısı 6 ama maç sayısı döngüde halledilebiliyor.5 sütun yeterli.



    for mac_say in range(takimin_toplam_mac_sayisi):
        devam='E'
        while devam in ['E','e']:
            print(mac_say+1,'.mac icin::')
            oyuncu_ad_soyad=input('Oyuncunun adini soyadini giriniz::')
            print('Oyuncunun pozisyonunu (1-5 arasi) giriniz')
            mevki=sayi_al(1,5)
            print('Oyuncunun attigi toplam sayiyi giriniz')
            skor=sayi_al(0,'*')     #Üst sınır yok.

            if oyuncu_ad_soyad not in oyuncu_skor_dict:     #Alternatifi: oyuncu_skor_dict[oyuncu_ad_soyad]=oyuncu_skor_dict.get(ad_soyad,0)+1'''
                oyuncu_skor_dict[oyuncu_ad_soyad]=skor      #Yoksa 0 atayıp 1'le toplar,varsa 1 arttırır.'''
            else:
                oyuncu_skor_dict[oyuncu_ad_soyad]+=skor

            mevki_skor_iki_boyutlu_listesi[mac_say][mevki-1]+=skor
            devam=input('Bu maca yeni oyuncu girmek icin E/e,siradaki maca gecmek icin E/e harici bir tus tuslayiniz::')

    print('\nMaclara iliskin girisleri tamamladiniz!Istatistikler asagida olusturuldu\n')

    print('Oyuncu adi-soyadi      ', '          Toplam sayi')
    print('------------------               --------------')
    for isim in oyuncu_skor_dict:
        print(format(isim, '39'), end='')
        print(oyuncu_skor_dict[isim])

    print('\nAtilan sayilarin mevkilere gore dagilimi \n')
    print('Mac no   Mevki-1   Mevki-2   Mevki-3   Mevki-4   Mevki-5')
    print('------   -------   -------   -------   -------   -------')
    for mac_no in range(takimin_toplam_mac_sayisi):
        print(format(mac_no+1,'3'),end='')
        for oyuncu_pozisyonu in range(5):
            print(format(mevki_skor_iki_boyutlu_listesi[mac_no][oyuncu_pozisyonu],'10'),end='')
        print('\n')



main()






