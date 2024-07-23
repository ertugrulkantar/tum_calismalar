def forma_no_hesapla():
    '''Forma numarasının basamak değerlerini alır,forma numarasını döndürür.'''
    hata_var_mi=True   #Flag.
    while hata_var_mi==True:
        try:
            birler_basamagi=int(input('Oyuncunun numarasinin birler basamagini giriniz::'))
            while birler_basamagi<0 or birler_basamagi>5:
                birler_basamagi=int(input('Hatali giris!Lutfen 0-5 degerleri arasinda bir rakam giriniz::'))
            hata_var_mi=False
        except ValueError:
            print('Deger hatasi!')
            hata_var_mi=True
        except:
            print('Hata!')
            hata_var_mi=True

    hata_var_mi=True    #Flag.
    while hata_var_mi==True:
        try:
            onlar_basamagi=int(input('Oyuncunun numarasinin onlar basamagini giriniz::'))
            while onlar_basamagi<0 or onlar_basamagi>5:
                onlar_basamagi=int(input('Hatali giris!Lutfen 0-5 degerleri arasinda bir rakam giriniz::'))
            hata_var_mi=False
        except ValueError:
            print('Deger hatasi!')
            hata_var_mi=True
        except:
            print('Hata!')
            hata_var_mi=True
    return onlar_basamagi*10+birler_basamagi



def oyuncu_skoru_al():
    '''Oyuncu skorunu alır ve döndürür.'''
    hata_var_mi=True    #Flag.
    while hata_var_mi==True:
        try:
            oyuncu_skoru=int(input('''Oyuncunun skorunu 1-3 araliginda giriniz veya cikis icin 0'i tuslayiniz::'''))
            while oyuncu_skoru<0 or oyuncu_skoru>3:
                oyuncu_skoru=int(input('''Hatali giris!0-3 araliginda deger giriniz veya cikis icin 0'i tuslayiniz::'''))
            hata_var_mi=False
        except ValueError:
            print('Deger hatasi!')
            hata_var_mi=True
        except:
            print('Hata!')
            hata_var_mi=True
    return  oyuncu_skoru



def main():
    '''Ana fonksiyon.'''
    skor_listesi=[0]*56                #Forma numaraları kombinasyonlarının oluşturabildiği maksimum forma numarası miktarı 36'dır.Ancak indexi
    oyuncu_skoru=oyuncu_skoru_al()     #probleme uyarlayabilmek için 56 elemanlı bir liste oluşturdum.
    if oyuncu_skoru!=0:
        forma_no=forma_no_hesapla()
    while oyuncu_skoru!=0:
        skor_listesi[forma_no]+=oyuncu_skoru    #try/except bloğu kullanmadım çünkü index değerleri daha önce hata oluşturmayacak şekilde
        oyuncu_skoru=oyuncu_skoru_al()          #alındı.
        if oyuncu_skoru!=0:
            forma_no=forma_no_hesapla()


    print('   Forma No', '       Sayi')
    print('  ----------', '     ------')
    for eleman in skor_listesi:
        if eleman!=0:
            print('      ',skor_listesi.index(eleman),sep='',end='')
            if skor_listesi.index(eleman)<10:   #Hizalama.
                print('              ',end='')
            else:                               #Hizalama.
                print('             ',end='')
            print(eleman)
            skor_listesi[skor_listesi.index(eleman)]=0        #Aynı değerde başka bir oyuncu numarası varsa,onu da yakalayabilmek için işlenen
                                                              #elemanı sıfırladım.



main()



def forma_no_hesapla2():        #Derste yapılan
    '''Forma numarasının basamak değerlerini alır,forma numarasını döndürür.'''
    hata_var_mi=True   #Flag.
    while hata_var_mi==True:
        try:
            birler_basamagi=int(input('Oyuncunun numarasinin birler basamagini giriniz::'))
            while birler_basamagi<0 or birler_basamagi>5:
                birler_basamagi=int(input('Hatali giris!Lutfen 0-5 degerleri arasinda bir rakam giriniz::'))
            hata_var_mi=False
        except ValueError:
            print('Deger hatasi!')
            hata_var_mi=True
        except:
            print('Hata!')
            hata_var_mi=True

    hata_var_mi=True    #Flag.
    while hata_var_mi==True:
        try:
            onlar_basamagi=int(input('Oyuncunun numarasinin onlar basamagini giriniz::'))
            while onlar_basamagi<0 or onlar_basamagi>5:
                onlar_basamagi=int(input('Hatali giris!Lutfen 0-5 degerleri arasinda bir rakam giriniz::'))
            hata_var_mi=False
        except ValueError:
            print('Deger hatasi!')
            hata_var_mi=True
        except:
            print('Hata!')
            hata_var_mi=True
    return onlar_basamagi*6+birler_basamagi     #6'lık sistem gibi düşün.

def main2():    #Derste anlatılan ve doğru olan
    '''Ana fonksiyon.'''
    skor_listesi=[0]*36
    oyuncu_skoru=oyuncu_skoru_al()
    if oyuncu_skoru!=0:
        forma_no=forma_no_hesapla2()
    while oyuncu_skoru!=0:
        skor_listesi[forma_no]+=oyuncu_skoru
        oyuncu_skoru=oyuncu_skoru_al()
        if oyuncu_skoru!=0:
            forma_no=forma_no_hesapla()


    print('   Forma No', '       Sayi')
    print('  ----------', '     ------')
    for index in range(len(skor_listesi)):
        if skor_listesi[index]!=0:
            print('      ',(index//6)*10,sep='',end='')
            if skor_listesi.index(eleman)<10:   #Hizalama.
                print('              ',end='')
            else:                               #Hizalama.
                print('             ',end='')
            print(eleman)
            skor_listesi[skor_listesi.index(eleman)]=0

