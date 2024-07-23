def menu_goruntule():
    print('1. Bul....')
    print('2. Tumunu Degistir...')
    print('3. Tek tek degistir...')
    print('0. Cikis...')
    print('Seciminizi giriniz[0-3]:',end='')

def sayi_al(alt_sinir,ust_sinir):
    try:
        sayi=int(input())
        hatali_giris=False
    except ValueError:      #Bütün hata türlerine ayrı exception yazmak tavsiye edilir.
        hatali_giris=True
    while hatali_giris==True or sayi<alt_sinir or sayi>ust_sinir:
        try:
            sayi=int(input('Hatali veri girisi,lutfen tekrar giriniz'))
            hatali_giris=False
        except ValueError:
            hatali_giris=True
    return sayi

def bul(metin,aranan):
    bulunma_say=0
    aranan_uzunluk=len(aranan)
    print('No Konum')
    print('-- -----')
    bulunan_konum=metin.find(aranan)
    while bulunan_konum!=-1:
        bulunma_say+=1
        print(bulunma_say,'  ',bulunan_konum+1)
        bulunan_konum=metin.find(aranan,bulunan_konum+aranan_uzunluk)       #İnce detay var,2.argümana dikkat!

def tumunu_degistir(metin,eski,yeni):
    return metin.replace(eski,yeni)

def evet_hayir_al():
    cevap=input()
    while cevap not in 'EeHh':
        cevap=input('Hatali veri girisi,lutfen tekrar giriniz:')
    return cevap


def tek_tek_degistir(metin,eski,yeni):
    aranan_uzunluk=len(eski)    #Değiştirilecek parçanın uzunluğu.
    arama_baslangici=0          #Cursor(imleç)'in nereye konumlanacağı.
    yeni_metin=''
    bulunan_konum=metin.find(eski,arama_baslangici)     #Değiştirileceğin konumu.
    while bulunan_konum!=-1:
        print(bulunan_konum+1,'.konumdaki degistirilsin mi(E/e/H/h)?',sep='',end='')
        degisim=evet_hayir_al()
        yeni_metin=yeni_metin+metin[arama_baslangici:bulunan_konum]
        if degisim in ['E','e']:
            yeni_metin=yeni_metin+yeni
        else:
            yeni_metin=yeni_metin+eski
        arama_baslangici=bulunan_konum+aranan_uzunluk   #Cursor+değiştirileceğin uzunluğu.
        bulunan_konum=metin.find(eski,arama_baslangici) #Yeniden cursor konumlandırma.
    yeni_metin=yeni_metin+metin[arama_baslangici:]      #Değişmeyen parçaları sona ekleme.
    return yeni_metin


def main():
    metin=input('Metninizi giriniz:')
    cikis='H'
    while cikis.upper()=='H':
        menu_goruntule()
        menu_secim=sayi_al(0,3)
        if menu_secim==1:
            aranan=input('Aradiginiz metin parçasını giriniz::')
            bul(metin,aranan)
        elif menu_secim==2:
            eski=input('Degistirmek istediginiz metin parcasini giriniz::')
            yeni=input('Yerine koymak istediginiz metin parcasini giriniz::')
            metin=tumunu_degistir(metin,eski,yeni)
            print(metin)
        elif menu_secim==3:
            eski = input('Degistirmek istediginiz metin parcasini giriniz::')
            yeni = input('Yerine koymak istediginiz metin parcasini giriniz::')
            metin=tek_tek_degistir(metin,eski,yeni)
            print(metin)
        else:
            print('Cikmak istediginizden emin misiniz(E/e/H/h)?',end='')
            cikis=evet_hayir_al()

main()