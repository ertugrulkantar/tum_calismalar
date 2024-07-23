def buyuk_harfe_donustur(kelime):
    '''Verilen kelimedeki harfleri büyük harfe dönüştürür.'''
    kelime_buyuk_harfli=''
    for harf in kelime:
        if harf=='i':
            harf='İ'
        elif harf=='ı':
            harf='I'
        else:
            harf=harf.upper()
        kelime_buyuk_harfli+=harf
    return kelime_buyuk_harfli


def harf_uzayi_matrisi_olustur():
    harf_uzayi_dosyasi=open('harf_uzayi.txt', 'r', encoding='utf-8')
    harf_uzayi_matris=[]
    harf_uzayi_islenecek_satir=(harf_uzayi_dosyasi.readline()).rstrip('\n')
    while harf_uzayi_islenecek_satir!="":
        harf_uzayi_matris.append(harf_uzayi_islenecek_satir)
        harf_uzayi_islenecek_satir=(harf_uzayi_dosyasi.readline()).rstrip('\n')
    harf_uzayi_dosyasi.close()
    return harf_uzayi_matris

harf_uzayi_matrisi=harf_uzayi_matrisi_olustur()

def uzayda_kelime_ara(kelime,harf_uzayi_matrisi):
    buyuk_harfli_kelime=buyuk_harfe_donustur(kelime)
    matris_satir_sayisi=len(harf_uzayi_matrisi)
    i=0     #Matrisin satır indexini simgeliyor.Aynı zamanda döngüde kelimenin ilk harfinin matristeki satır indexi.
    dongulerde_kullanilacak_satir_indexi=i
    harf_konum_tupleleri_listesi=[]
    while i<matris_satir_sayisi:
        aranacak_satir=harf_uzayi_matrisi[i]
        j=aranacak_satir.find(buyuk_harfli_kelime[0])    #Kelimenin ilk harfinin matristeki sütun indexi.
        dongulerde_kullanilacak_sutun_indexi=j
        if j==-1:
            i+=1
            continue
        else:
            harf_bulundu=True

        while harf_bulundu==True:
            dongulerde_kullanilacak_satir_indexi=i
            dongulerde_kullanilacak_sutun_indexi=j
            try:
                for harf in buyuk_harfli_kelime:
                    if harf==harf_uzayi_matrisi[dongulerde_kullanilacak_satir_indexi][dongulerde_kullanilacak_sutun_indexi] and dongulerde_kullanilacak_satir_indexi>=0 and dongulerde_kullanilacak_sutun_indexi>=0:
                        dongulerde_kullanilacak_sutun_indexi+=1
                    else:
                        hata_yap
            except:
                pass
            else:
                harf_konum_tuplesi=(i+1,j+1,3)
                harf_konum_tupleleri_listesi.append(harf_konum_tuplesi)

            dongulerde_kullanilacak_satir_indexi=i
            dongulerde_kullanilacak_sutun_indexi=j
            try:
                for harf in buyuk_harfli_kelime:
                    if harf==harf_uzayi_matrisi[dongulerde_kullanilacak_satir_indexi][dongulerde_kullanilacak_sutun_indexi] and dongulerde_kullanilacak_satir_indexi>=0 and dongulerde_kullanilacak_sutun_indexi>=0:
                        dongulerde_kullanilacak_sutun_indexi-=1
                    else:
                        hata_yap    #
            except:
                pass
            else:
                harf_konum_tuplesi=(i+1,j+1,7)
                harf_konum_tupleleri_listesi.append(harf_konum_tuplesi)

            dongulerde_kullanilacak_satir_indexi=i
            dongulerde_kullanilacak_sutun_indexi=j
            try:
                for harf in buyuk_harfli_kelime and dongulerde_kullanilacak_satir_indexi>=0 and dongulerde_kullanilacak_sutun_indexi>=0:
                    if harf==harf_uzayi_matrisi[dongulerde_kullanilacak_satir_indexi][dongulerde_kullanilacak_sutun_indexi]:
                        dongulerde_kullanilacak_satir_indexi+=1
                    else:
                        hata_yap
            except:
                pass
            else:
                harf_konum_tuplesi=(i+1,j+1,5)
                harf_konum_tupleleri_listesi.append(harf_konum_tuplesi)

            dongulerde_kullanilacak_satir_indexi=i
            dongulerde_kullanilacak_sutun_indexi=j
            try:
                for harf in buyuk_harfli_kelime:
                    if harf==harf_uzayi_matrisi[dongulerde_kullanilacak_satir_indexi][dongulerde_kullanilacak_sutun_indexi] and dongulerde_kullanilacak_satir_indexi>=0 and dongulerde_kullanilacak_sutun_indexi>=0:
                        dongulerde_kullanilacak_satir_indexi-=1
                    else:
                        hata_yap
            except:
                pass
            else:
                harf_konum_tuplesi=(i+1,j+1,1)
                harf_konum_tupleleri_listesi.append(harf_konum_tuplesi)

            dongulerde_kullanilacak_satir_indexi=i
            dongulerde_kullanilacak_sutun_indexi=j
            try:
                for harf in buyuk_harfli_kelime:
                    if harf==harf_uzayi_matrisi[dongulerde_kullanilacak_satir_indexi][dongulerde_kullanilacak_sutun_indexi] and dongulerde_kullanilacak_satir_indexi>=0 and dongulerde_kullanilacak_sutun_indexi>=0:
                        dongulerde_kullanilacak_satir_indexi_indexi+=1
                        dongulerde_kullanilacak_sutun_indexi+=1
                    else:
                        hata_yap
            except:
                pass
            else:
                harf_konum_tuplesi=(i+1,j+1,4)
                harf_konum_tupleleri_listesi.append(harf_konum_tuplesi)

            dongulerde_kullanilacak_satir_indexi=i
            dongulerde_kullanilacak_sutun_indexi=j
            try:
                for harf in buyuk_harfli_kelime:
                    if harf==harf_uzayi_matrisi[dongulerde_kullanilacak_satir_indexi][dongulerde_kullanilacak_sutun_indexi] and dongulerde_kullanilacak_satir_indexi>=0 and dongulerde_kullanilacak_sutun_indexi>=0:
                        dongulerde_kullanilacak_satir_indexi-=1
                        dongulerde_kullanilacak_sutun_indexi+=1
                    else:
                        hata_yap
            except:
                pass
            else:
                harf_konum_tuplesi=(i+1,j+1,2)
                harf_konum_tupleleri_listesi.append(harf_konum_tuplesi)

            dongulerde_kullanilacak_satir_indexi=i
            dongulerde_kullanilacak_sutun_indexi=j
            try:
                for harf in buyuk_harfli_kelime:
                    if harf==harf_uzayi_matrisi[dongulerde_kullanilacak_satir_indexi][dongulerde_kullanilacak_sutun_indexi] and dongulerde_kullanilacak_satir_indexi>=0 and dongulerde_kullanilacak_sutun_indexi>=0:
                        dongulerde_kullanilacak_satir_indexi+=1
                        dongulerde_kullanilacak_sutun_indexi-=1
                    else:
                        hata_yap
            except:
                pass
            else:
                harf_konum_tuplesi=(i+1,j+1,6)
                harf_konum_tupleleri_listesi.append(harf_konum_tuplesi)

            dongulerde_kullanilacak_satir_indexi=i
            dongulerde_kullanilacak_sutun_indexi=j
            try:
                for harf in buyuk_harfli_kelime:
                    if harf==harf_uzayi_matrisi[dongulerde_kullanilacak_satir_indexi][dongulerde_kullanilacak_sutun_indexi] and dongulerde_kullanilacak_satir_indexi>=0 and dongulerde_kullanilacak_sutun_indexi>=0:
                        dongulerde_kullanilacak_satir_indexi-=1
                        dongulerde_kullanilacak_sutun_indexi-=1
                    else:
                        hata_yap
            except:
                pass
            else:
                harf_konum_tuplesi=(i+1,j+1,8)
                harf_konum_tupleleri_listesi.append(harf_konum_tuplesi)

            j=aranacak_satir.find(buyuk_harfli_kelime[0],j+1)    #Bu satırda kelimenin ilk harfinden daha da var mı diye kontrol.
            if j==-1:
                harf_bulundu=False
                i+=1
            else:
                harf_bulundu=True

    if len(harf_konum_tupleleri_listesi)==0:
        return 'BULUNAMADI'
    else:
        return harf_konum_tupleleri_listesi












print(uzayda_kelime_ara('adana',harf_uzayi_matrisi))