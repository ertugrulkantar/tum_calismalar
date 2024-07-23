def kelime_tekrari_tablo_sablonu():
    '''Kelime tekrarı tabloları için şablon.'''
    print(format('Kelime','22'),format('Tekrar Say','10'),'|',format('Kelime','22'),format('Tekrar Say','10'))
    print(format('------','22'),format('----------','10'),'|',format('------','22'),format('----------','10'))

def harf_konum_tablo_sablonu():
    '''Harf konum tablosu için şablon.'''
    print(format('Harf','5'),end='')
    for i in range(1,21):
        print(format(i,'5'),end='')
    print('      Toplam')
    print('----   ',end='')
    for i in range(20):
        print('---- ',end='')
    print('    ------')


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

def tekrar_sayisina_gore_sirala(dict_siralanacak):
    '''Sözlüğü tekrar sayısına göre sıralar.'''
    key_value_listesi=[]
    for key,value in dict_siralanacak.items():
        key_value_cifti=[key,value]
        key_value_listesi.append(key_value_cifti)
    key_value_listesi.sort(key=lambda pair:pair[1])
    key_value_listesi.reverse()
    return key_value_listesi

def sozluk_sirala(dict_siralanacak):
    '''Buble sort yöntemiyle girilen sözlüğü sıralı hale getirir.'''
    harfler="ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ,"
    dict_liste=list(dict_siralanacak)
    liste_uzunlugu=len(dict_liste)
    yapilacak_karsilastirma_sayisi=liste_uzunlugu-1
    i=0

    while yapilacak_karsilastirma_sayisi!=0:
        incelenecek_harf_index=0
        ilk_kelime=dict_liste[i]
        if i==0:
            swap_yapildi_mi=False
            yapilan_karsilastirma_sayisi=0
        try:
            ikinci_kelime=dict_liste[i+1]
        except:
            yapilacak_karsilastirma_sayisi-=1
            i=0
            if swap_yapildi_mi==False:  #Eğer listenin sonuna gelinmişse ve hala swap yapılmamışsa
                break                   #sıralamayı sonlandırabiliriz.
            continue                    #Öyle değilse devam edebiliriz.

        flag=True
        ilk_kelime_harf_sayisi=len(ilk_kelime)
        ikinci_kelime_harf_sayisi=len(ikinci_kelime)
        while flag==True and yapilan_karsilastirma_sayisi<=yapilacak_karsilastirma_sayisi:
            try:
                ilk_kelime_incelenecek_harf=ilk_kelime[incelenecek_harf_index]
                ikinci_kelime_incelenecek_harf=ikinci_kelime[incelenecek_harf_index]
                ilk_kelime_incelenecek_harf_alfabe_degeri=harfler.index(ilk_kelime_incelenecek_harf)
                ikinci_kelime_incelenecek_harf_alfabe_degeri=harfler.index(ikinci_kelime_incelenecek_harf)
                if ilk_kelime_incelenecek_harf_alfabe_degeri>ikinci_kelime_incelenecek_harf_alfabe_degeri:
                    dict_liste[i],dict_liste[i+1]=dict_liste[i+1],dict_liste[i]
                    flag=False
                    swap_yapildi_mi=True
                elif ikinci_kelime_incelenecek_harf_alfabe_degeri>ilk_kelime_incelenecek_harf_alfabe_degeri:
                    pass    #Swap yapma.
                    flag=False
                else:
                    incelenecek_harf_index+=1
                    flag=True
            except:
                if ilk_kelime_harf_sayisi>ikinci_kelime_harf_sayisi:
                    dict_liste[i],dict_liste[i+1]=dict_liste[i+1],dict_liste[i]
                    flag=False
                    swap_yapildi_mi=True
                else:
                    flag=False
        i+=1
        yapilan_karsilastirma_sayisi+=1
    return dict_liste

def harf_konum_listesi_olustur():
    '''Kelimelerin işleneceği harf-konum listesini oluşturur ve döndürür.'''
    harf_say_liste=[]
    for i in range(29):     #29 harf için 29 satır.
        bir_harf=[0]*20
        harf_say_liste.append(bir_harf)
    return harf_say_liste

def harf_konum_listesine_kelime_isle(kelime,harf_say_liste):
    '''Kelimeleri harf-konum listesindeki uygun konumlara işler.'''
    turkce_alfabe='ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    harf_say=-1
    for harf in kelime:
        harf_say+=1     #Harfin işleneceği sütun konumunu simgeler.
        turkce_alfabedeki_index=turkce_alfabe.index(harf)   #Harfin işleneceği satır konumunu simgeler.
        harf_say_liste[turkce_alfabedeki_index][harf_say]+=1
    return harf_say_liste

def son_kelime_haric_her_kelime_sonuna_bosluk_ekle(satirdaki_kelimelerin_listesi):
    '''Kelimeler split ile bölündüğünden boşluk içermiyor,içermeli.Sadece son kelimenin sonunda boşluk olmaması gerekiyor.Fonksiyon bunları hallediyor'''
    satirdaki_kelimeler_tek_bosluk_ayarli_liste=[]
    for i in range(len(satirdaki_kelimelerin_listesi)):
        if i!=len(satirdaki_kelimelerin_listesi):
            bosluk_ayarli_kelime=satirdaki_kelimelerin_listesi[i]+' '
            satirdaki_kelimeler_tek_bosluk_ayarli_liste.append(bosluk_ayarli_kelime)
        else:
            son_kelime=satirdaki_kelimelerin_listesi[-1]
            satirdaki_kelimeler_tek_bosluk_ayarli_liste.append(son_kelime)
    return satirdaki_kelimeler_tek_bosluk_ayarli_liste

def bosluklari_dagit(kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste,satir_genisligi,satir_no_say,olmasi_gereken_satir_genisligi):
    '''Boşlukları satır numarasına ve genişliğine göre uygun şekilde dağıtıyor.Son satırsa veya kelime satırda tek kalmalıysa bunu sondaki 'else' hallediyor.'''
    bosluk_karakteri=' '
    if satir_no_say%2==1 and satir_no_say!=-1 and len(kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste)!=1:
        j=0
        while satir_genisligi<olmasi_gereken_satir_genisligi:
            kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste[j]=kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste[j]+bosluk_karakteri
            satir_genisligi+=1
            j=j+1
            if len(kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste)-1==j:
                j=0
    elif satir_no_say%2==0 and satir_no_say!=-1 and len(kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste)!=1:
        k=-1
        while satir_genisligi<olmasi_gereken_satir_genisligi:
            kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste[k]=bosluk_karakteri+kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste[k]
            satir_genisligi+=1
            k=k-1
            if kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste[k]==kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste[0]:
                k=-1
    else:   #Satır sonuna gelinmişse yani satir_no_say==-1 ise veya satırda tek kelime var ise
        pass    #Hiçbir şey yapma.
    bosluklari_ayarlanmis_liste=kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste.copy()   #Direkt olarak kopyası alınan liste de gönderilebilir.
    return bosluklari_ayarlanmis_liste                                                      #Ancak yine anlaşılırlığı arttırmak için liste adını değiştirildi.

def harf_uzayi_matrisi_olustur():
    harf_uzayi_dosyasi=open('harf_uzayi.txt', 'r', encoding='utf-8')
    harf_uzayi_matris=[]
    harf_uzayi_islenecek_satir=(harf_uzayi_dosyasi.readline()).rstrip('\n')
    while harf_uzayi_islenecek_satir!="":
        harf_uzayi_matris.append(harf_uzayi_islenecek_satir)
        harf_uzayi_islenecek_satir=(harf_uzayi_dosyasi.readline()).rstrip('\n')
    harf_uzayi_dosyasi.close()
    return harf_uzayi_matris



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
        if j==-1:   #Satırda mevcut değilse
            i+=1    #Diğer satıra geç ve döngüyü başa sar.
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
                        hata_yap    #Burada ve diğer döngülerde akışı bilerek except'e yöneltmek için
            except:                 #exception oluşturdum.
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
                        hata_yap
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
                        dongulerde_kullanilacak_satir_indexi+=1
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
                harf_bulundu=False  #Yok ise döngüden çıkıp
                i+=1                #diğer satır ile üstte uğraşıyor.
            else:
                harf_bulundu=True   #Bulursa dönmeye devam ediyor.

    return harf_konum_tupleleri_listesi

def harf_uzayi_aramasi_tuple_inin_ikinci_indexini_adlandir_ve_yazdir(sayi):
    if sayi==1:
        print('Kuzey')
    elif sayi==2:
        print('Kuzeydogu')
    elif sayi==3:
        print('Dogu')
    elif sayi==4:
        print('Guneydogu')
    elif sayi==5:
        print('Guney')
    elif sayi==6:
        print('Guneybati')
    elif sayi==7:
        print('Bati')
    else:
        print('Kuzeybati')

def main():
    i=0
    satir_no_say=0
    dict_lokal={}
    dict_global={}
    harf_say_liste=harf_konum_listesi_olustur()     #Bu liste 'harf_konum_listesine_eleman_isle' fonksiyonuna argüman olarak verilecek.
    metin=input('Metni giriniz::')
    liste=metin.split()
    olmasi_gereken_satir_uzunlugu=int(input('Satir uzunlugunu giriniz::'))
    flag=True   #2.while'a ilk giriş için atama.
    while olmasi_gereken_satir_uzunlugu!=0:
        satir=''
        while flag==True:
            try:
                kelime_eklenecek=' '+liste[i]
            except:
                break
            satir=satir+kelime_eklenecek
            if satir[0]==' ':   #Kelimeleri satıra eklerken boşlukları kelimelerin sağına değil soluna koydum.Bu satırın ilk karakteri için problem oluşturuyor,
                satir=satir.lstrip()    #Bu sebeple ilk karakter boşluk ise onu silmeliyim.
            try:
                kelime_sonraki=' '+liste[i+1]
            except:
                satir_no_say=-1  #Eğer bir sonraki kelime yok ise satır sonu gelmiş demektir.Bunu saçma bir değer yaparak 'bosluklari_dagit' fonksiyonunda
                break            #son satırı ayırt edebilmek için kullandım.
            sonraki_satir_uzunlugu=len(satir)+len(kelime_sonraki)
            if sonraki_satir_uzunlugu<=olmasi_gereken_satir_uzunlugu:
                flag=True   #Satır dolmamış ve sıradaki kelime boşluğu ile birlikte satıra sığıyor.Devam edilmeli.
                i+=1
            else:
                flag=False  #Satır tamamlandı.
                satir_no_say+=1 #O yüzden artık kaçıncı satır olduğunu saydırabilirim.

        satir_genisligi=len(satir)
        satirdaki_kelimelerin_listesi=satir.split()
        kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste=son_kelime_haric_her_kelime_sonuna_bosluk_ekle(satirdaki_kelimelerin_listesi)
        bosluklari_ayarlanmis_kelimeler_liste=bosluklari_dagit(kelimeler_arasi_tek_bosluk_olarak_ayarlanmis_liste,satir_genisligi,satir_no_say,olmasi_gereken_satir_uzunlugu)
        for el in bosluklari_ayarlanmis_kelimeler_liste:
            print(el,end='')
        print('\n',end='')
        if satir_no_say!=-1:
            flag=True
            i+=1
        else:
            olmasi_gereken_satir_uzunlugu=int(input('''Metni yeni bir satir uzunluguyla goruntulemek icin bir deger giriniz veya cikis icin 0'i tuslayiniz'''))
            if olmasi_gereken_satir_uzunlugu!=0:
                i=0     #Metni satır genişliğine göre tekrar düzenleyebilmek için bu
                satir_no_say=0  #ve bu değişkenler sıfırlandı.
                flag=True   #2.while'a tekrar giriş için atama.
        if olmasi_gereken_satir_uzunlugu==0:
            print('Satir uzunlugunu 0 girdiniz.Metnin kelime istatistikleri aşağıda oluşturuldu.')
            print('\n')
            for eleman in liste:
                buyuk_harfli_kelime=buyuk_harfe_donustur(eleman)
                dict_lokal[buyuk_harfli_kelime]=dict_lokal.get(buyuk_harfli_kelime,0)+1
                dict_global[buyuk_harfli_kelime]=dict_global.get(buyuk_harfli_kelime,0)+1
                harf_konum_listesine_kelime_isle(buyuk_harfli_kelime,harf_say_liste)
            local_dict_in_alfabetik_siralanmis_key_listesi=sozluk_sirala(dict_lokal)
            local_dict_in_tekrar_sayisina_gore_siralanmis_listesi = tekrar_sayisina_gore_sirala(dict_lokal)
            kelime_tekrari_tablo_sablonu()
            for i in range(len(local_dict_in_alfabetik_siralanmis_key_listesi)):    #Sözcük sayısı kadar eleman yazdıracağız her ikisi için de.
                alfabetik_siralanmis_kelime=local_dict_in_alfabetik_siralanmis_key_listesi[i]
                tekrar_sayisina_gore_siralanmis_kelime=local_dict_in_tekrar_sayisina_gore_siralanmis_listesi[i][0]
                print(format(alfabetik_siralanmis_kelime,'22'),format(dict_lokal[alfabetik_siralanmis_kelime],'6'),'    | ',end='')
                print(format(tekrar_sayisina_gore_siralanmis_kelime,'23'),format(dict_lokal[tekrar_sayisina_gore_siralanmis_kelime],'5'))
            print('\n')
            yeni_metinle_devam=input('Yeni bir metin girerek devam etmek ister misiniz(E/e/H/h)::')
            if yeni_metinle_devam=='E' or yeni_metinle_devam=='e':
                metin=input('Metni giriniz::')
                olmasi_gereken_satir_uzunlugu=int(input('''Satir uzunlugunu '0' haric bir deger giriniz::'''))
                liste=metin.split()
                dict_lokal={}
                i=0
                satir_no_say=0
    print('\n')
    print('Metin girislerini tamamladiniz.Tum metinlerle alakali tablo ve istatistikler asagida olusturuldu.')
    print('\n')

    kelime_tekrari_tablo_sablonu()
    global_dict_in_alfabetik_siralanmis_key_listesi=sozluk_sirala(dict_global)
    global_dict_in_tekrar_sayisina_gore_siralanmis_listesi=tekrar_sayisina_gore_sirala(dict_global)
    for i in range(len(global_dict_in_alfabetik_siralanmis_key_listesi)):  #Sözcük sayısı kadar eleman yazdıracağız her ikisi için de.
        alfabetik_siralanmis_kelime = global_dict_in_alfabetik_siralanmis_key_listesi[i]
        tekrar_sayisina_gore_siralanmis_kelime=global_dict_in_tekrar_sayisina_gore_siralanmis_listesi[i][0]
        print(format(alfabetik_siralanmis_kelime, '22'), format(dict_global[alfabetik_siralanmis_kelime],'6'),'    | ',end='')
        print(format(tekrar_sayisina_gore_siralanmis_kelime, '23'),format(dict_global[tekrar_sayisina_gore_siralanmis_kelime], '5'))
    print('\n')


    harf_konum_tablo_sablonu()
    turkce_alfabe='ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    for i in range(len(turkce_alfabe)):
        print('',turkce_alfabe[i],'  ',end='')
        goruntulenecek_satir=harf_say_liste[i]
        for i in goruntulenecek_satir:
            print(format(i,'5'),end='')
        print('       ',format(sum(goruntulenecek_satir),'<5'))



    harf_uzayi_matrisi=harf_uzayi_matrisi_olustur()
    print('\n')
    print(format('Kelime','25'),format('Satir No','10'),format('Sutun No','10'),format('Yonu','8'))
    print('--------------------      --------   --------  ------')
    for el in dict_global.keys():
        harf_uzay_konum_listesi=list(uzayda_kelime_ara(el,harf_uzayi_matrisi))
        if len(harf_uzay_konum_listesi)!=0:
            for tuple1 in harf_uzay_konum_listesi:
                print(format(el,'29'),format(tuple1[0],'<10'),format(tuple1[1],'<7'),end='')
                tuple1_index_2_degeri=int(tuple1[2])
                harf_uzayi_aramasi_tuple_inin_ikinci_indexini_adlandir_ve_yazdir(tuple1_index_2_degeri)
        else:
            print(format(el,'25'),'BULUNAMADI')

main()