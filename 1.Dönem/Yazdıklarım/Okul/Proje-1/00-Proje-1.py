#Sayacı en başta almamamın sebebi proje forumunda bunun tartışılması ve hocamızın
#pdf'deki sıraya uymamızı istemesidir.

#Şehit-sporcu indirimlerinde programı etkilemediği için
#her ikisini de 'S/s' seçiminde topladım.

KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI=2.89
KONUT_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI=3.13
KONUT_TIPI_3_UNCU_KADEME_SU_TUKETIM_BIRIM_UCRETI=6.43
KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI=1.44
KONUT_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI=1.56
KONUT_TIPI_3_UNCU_KADEME_ATIK_SU_BIRIM_UCRETI=3.22

KONUT_TIPI_1_INCI_KADEME_SINIRI=13
KONUT_TIPI_2_INCI_KADEME_SINIRI=20

ISYERI_TIPI_SU_TUKETIM_BIRIM_UCRETI=7.38
ISYERI_TIPI_ATIK_SU_BIRIM_UCRETI=3.68

RESMI_DAIRE_TIPI_SU_TUKETIM_BIRIM_UCRETI=4.34
RESMI_DAIRE_TIPI_ATIK_SU_BIRIM_UCRETI=2.16

ORGANIZE_SANAYI_TIPI_SU_TUKETIM_BIRIM_UCRETI=5
ORGANIZE_SANAYI_TIPI_ATIK_SU_BIRIM_UCRETI=2.5

ILCE_TARIMSAL_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETİ=1.45
ILCE_TARIMSAL_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETİ=2.89
ILCE_TARIMSAL_TIPI_3_UNCU_KADEME_SU_TUKETIM_BIRIM_UCRETİ=6.43
ILCE_TARIMSAL_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI=0.72
ILCE_TARIMSAL_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI=1.44
ILCE_TARIMSAL_TIPI3_UNCU_KADEME_ATIK_SU_BIRIM_UCRETI=3.22

ILCE_TARIMSAL_1_INCI_KADEME_SINIRI=13
ILCE_TARIMSAL_2_INCI_KADEME_SINIRI=20

YIRMI_TONA_KADAR_ENGELLI_INDIRIMI=0.5
SEHIT_GAZI_SPORCU_INDIRIMI=0.5

KDV=0.08
TON_BASINA_CTV=0.39
HANE_BASI_KATI_ATIK_TOPLAMA_UCRETİ=13
HANE_BASI_KATI_ATIK_BERTARAF_UCRETİ=2.54

hane_tipi_abone_sayisi=0
isyeri_tipi_abone_sayisi=0
resmi_daire_tipi_abone_sayisi=0
organize_sanayi_tipi_abone_sayisi=0
ilce_tarimsal_ve_hayvansal_sulama_tipi_abone_sayisi=0
hane_aylik_su_tuketim_toplami=0
isyeri_aylik_su_tuketim_toplami=0
resmi_daire_aylik_su_tuketim_toplami=0
organize_sanayi_aylik_su_tuketim_toplami=0
ilce_tarimsal_ve_hayvansal_aylik11_su_tuketim_toplami=0
hane_kademe_1=0
hane_kademe_1_aylik_su_tuketimi=0
hane_kademe_2=0
hane_kademe_2_aylik_su_tuketimi=0
hane_kademe_3=0
hane_kademe_3_aylik_su_tuketimi=0
elli_tondan_fazla_su_tuketen_ilce_tarimsal_hayvansal=0
cok_su_tuketen_aboneler=0
indirimli_abone_sayisi=0
resmi_daire_max_su_tuketimi=0
max_tuketim_yapan_konut_disi_abonenin_ucreti=0
hane_aylik_su_tuketim_ucreti=0
isyeri_aylik_su_tuketim_ucreti=0
resmi_daire_aylik_su_tuketim_ucreti=0
organize_sanayi_aylik_su_tuketim_ucreti=0
ilce_tarimsal_ve_hayvansal_sulama_su_tuketim_ucreti=0
toplam_izsu_payi=0
toplam_ilce_belediyesi_payi=0
toplam_buyuksehir_belediyesi_payi=0
toplam_devlet_payi=0
toplu_hane_carpani=1
max_tuketim_yapan_abonenin_nosu=0
hane_sayisi=0




devam='E'
while devam=='E' or devam=='e':
    abone_tipi = int(input('''Konut tipi abone icin 1'i
    İsyeri tipi abone icin 2'yi
    Resmi daire tipi abone icin 3'u
    Organize sanayi tipi abone icin 4'u
    İlce tarimsal ve hayvansal sulama tipi abone icin 5'i tuslayiniz::\n'''))

    while not (0 < abone_tipi < 6):
        print('Hatali giris!')
        print('Lutfen 1,2,3,4,5 numarali tiplerden birini tuslayiniz::')
        abone_tipi = int(input())

    abone_no = int(input('Abone numaranızı giriniz::'))

    if abone_tipi==1:
        abone_tipi_adi='Hane tipi abone'
        toplu_hane_carpani=1
        hane_sayisi=int(input('Lutfen hane sayinizi giriniz::'))

        while hane_sayisi<1:
            hane_sayisi=int(input('''Hatali giris.Lutfen 0'dan buyuk bir tam sayi giriniz::'''))
        if hane_sayisi==1:
            hane_tipi_abone_sayisi +=hane_sayisi
            print('İndirim durumunuz varsa sehit yakinlari icin::s/S')  #Şehit yakını,sporcu s/S olarak alındı.
            print('Gaziler icin::g/G')
            print('Sporcular icin::s/S')
            print('Yok secenegi icin::y/Y tuslayiniz::')
            indirim_durumu=input('')
            if indirim_durumu!='y' and indirim_durumu!='Y':
                indirimli_abone_sayisi+=1

            onceki_sayac_degeri = int(input('Onceki sayac degerini giriniz::'))
            while onceki_sayac_degeri < 0:
                print('Hatali giris.')
                onceki_sayac_degeri = int(input('Lutfen onceki sayac degerini tekrar giriniz::'))
            simdiki_sayac_degeri = int(input('Simdiki sayac degerini giriniz::'))
            while simdiki_sayac_degeri < onceki_sayac_degeri:
                print('Hatali giris.')
                simdiki_sayac_degeri = int(input('Lutfen simdiki sayac degerini tekrar giriniz::'))
            donemlik_su_tuketimi=simdiki_sayac_degeri-onceki_sayac_degeri
            sayac_okunmada_gun_araligi = int(input('Sayacinizin kac gun aralikla okundugunu giriniz::'))
            while sayac_okunmada_gun_araligi < 1:
                sayac_okunmada_gun_araligi = int(input('''Hatali giris.Lutfen 0'dan buyuk bir deger giriniz::'''))


            aylik_sinirlari_donemlik_sinirlara_cevirme_carpani=sayac_okunmada_gun_araligi/30
            donemlik_1_inci_kademe_siniri=KONUT_TIPI_1_INCI_KADEME_SINIRI*aylik_sinirlari_donemlik_sinirlara_cevirme_carpani
            donemlik_2_inci_kademe_siniri=KONUT_TIPI_2_INCI_KADEME_SINIRI*aylik_sinirlari_donemlik_sinirlara_cevirme_carpani

            if 0<=donemlik_su_tuketimi<=donemlik_1_inci_kademe_siniri:
                hane_kademe_1+=hane_sayisi
                hane_kademe_1_aylik_su_tuketimi+=donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi     #dönemi aylığa çevirme.

                donemlik_su_tuketim_ucreti=donemlik_su_tuketimi*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI
                donemlik_atik_su_ucreti=donemlik_su_tuketimi*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI
                if indirim_durumu=='E' or indirim_durumu=='e':
                    donemlik_su_tuketim_ucreti*=YIRMI_TONA_KADAR_ENGELLI_INDIRIMI
                    donemlik_atik_su_ucreti*=YIRMI_TONA_KADAR_ENGELLI_INDIRIMI
                if indirim_durumu=='S' or indirim_durumu=='s' or indirim_durumu=='G' or indirim_durumu=='g':
                    donemlik_su_tuketim_ucreti*=SEHIT_GAZI_SPORCU_INDIRIMI
                    donemlik_atik_su_ucreti*=SEHIT_GAZI_SPORCU_INDIRIMI
            elif donemlik_1_inci_kademe_siniri<donemlik_su_tuketimi<=donemlik_2_inci_kademe_siniri:
                hane_kademe_2 += hane_sayisi
                hane_kademe_2_aylik_su_tuketimi += donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi #dönemi aylığa çevirme.
                ikinci_kademeye_kalan_su_miktari=donemlik_su_tuketimi-donemlik_1_inci_kademe_siniri
                donemlik_su_tuketim_ucreti=donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI
                donemlik_atik_su_ucreti=donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI
                if indirim_durumu=='E' or indirim_durumu=='e':
                    donemlik_su_tuketim_ucreti*=YIRMI_TONA_KADAR_ENGELLI_INDIRIMI
                    donemlik_atik_su_ucreti*=YIRMI_TONA_KADAR_ENGELLI_INDIRIMI
                if indirim_durumu=='S' or indirim_durumu=='s' or indirim_durumu=='G' or indirim_durumu=='g':
                    donemlik_su_tuketim_ucreti*=SEHIT_GAZI_SPORCU_INDIRIMI
                    donemlik_atik_su_ucreti*=SEHIT_GAZI_SPORCU_INDIRIMI
            else:
                hane_kademe_3 += hane_sayisi
                hane_kademe_3_aylik_su_tuketimi += donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi    #dönemi aylığa çevirme.

                ucuncu_kademeye_kalan_su_miktari=donemlik_su_tuketimi-donemlik_2_inci_kademe_siniri
                ikinci_kademeye_kalan_su_miktari=donemlik_su_tuketimi-ucuncu_kademeye_kalan_su_miktari-donemlik_1_inci_kademe_siniri

                donemlik_su_tuketim_ucreti=donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI+ucuncu_kademeye_kalan_su_miktari*KONUT_TIPI_3_UNCU_KADEME_SU_TUKETIM_BIRIM_UCRETI
                donemlik_atik_su_ucreti=donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI+ucuncu_kademeye_kalan_su_miktari*KONUT_TIPI_3_UNCU_KADEME_ATIK_SU_BIRIM_UCRETI
                if indirim_durumu=='S' or indirim_durumu=='s' or indirim_durumu=='G' or indirim_durumu=='g':
                    donemlik_su_tuketim_ucreti*=SEHIT_GAZI_SPORCU_INDIRIMI
                    donemlik_atik_su_ucreti*=SEHIT_GAZI_SPORCU_INDIRIMI
                if indirim_durumu=='E' or indirim_durumu=='e':
                    donemlik_su_tuketim_ucreti=(donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI)*YIRMI_TONA_KADAR_ENGELLI_INDIRIMI+ucuncu_kademeye_kalan_su_miktari*KONUT_TIPI_3_UNCU_KADEME_SU_TUKETIM_BIRIM_UCRETI
                    donemlik_atik_su_ucreti=(donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI)*YIRMI_TONA_KADAR_ENGELLI_INDIRIMI+ucuncu_kademeye_kalan_su_miktari*KONUT_TIPI_3_UNCU_KADEME_ATIK_SU_BIRIM_UCRETI

            hane_aylik_tuketim_cevirmesi=donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi
            hane_aylik_su_tuketim_toplami+=hane_aylik_tuketim_cevirmesi
            hane_basi_ortalama_tuketim=donemlik_su_tuketimi






        if hane_sayisi>1:
            hane_tipi_abone_sayisi+=hane_sayisi
            toplu_hane_carpani=hane_sayisi
            sehit_gazi_sporcu_sayisi=int(input('Apartmaninizdaki sehit yakini,gazi ve sporcu indirimli haneler sayisini giriniz::'))
            while sehit_gazi_sporcu_sayisi<0 or sehit_gazi_sporcu_sayisi>hane_sayisi:
                print('Hatali veya hane sayisiyla tutarsiz giris.')
                sehit_gazi_sporcu_sayisi=int(input('Lutfen apartmaninizdaki sehit yakini,gazi ve sporcu indirimli hane sayisini tekrar giriniz::'))
            engelli_sayisi=int(input('Apartmaninizdaki engelli indirimli hane sayisini giriniz::'))
            while engelli_sayisi<0 or engelli_sayisi>hane_sayisi:
                print('Hatali veya hane sayisiyla tutarsiz giris.')
                engelli_sayisi=int(input('Lutfen apartmaninizdaki engelli indirimli hane sayi sayisini tekrar giriniz::'))
            while engelli_sayisi+sehit_gazi_sporcu_sayisi>hane_sayisi:
                print('İndirimli hane sayisi toplami toplam hane sayisindan buyuk!')
                sehit_gazi_sporcu_sayisi=int(input('Sehit yakini,gazi ve sporcu indirimli hane sayisini tekrar giriniz::'))
                while sehit_gazi_sporcu_sayisi < 0 or sehit_gazi_sporcu_sayisi > hane_sayisi:
                    print('Hatali veya hane sayisiyla tutarsiz giris.')
                    sehit_gazi_sporcu_sayisi = int(input('Lutfen apartmaninizdaki sehit yakini,gazi ve sporcu indirimli hane sayisini tekrar giriniz::'))
                engelli_sayisi=int(input('Engelli indirimli hane sayisini tekrar giriniz::'))
                while engelli_sayisi < 0 or engelli_sayisi > hane_sayisi:
                    print('Hatali veya hane sayisiyla tutarsiz giris.')
                    engelli_sayisi = int(input('Lutfen apartmaninizdaki engelli indirimli hane sayi sayisini tekrar giriniz::'))
            indirimli_abone_sayisi+=sehit_gazi_sporcu_sayisi+engelli_sayisi
            onceki_sayac_degeri = int(input('Onceki sayac degerini giriniz::'))
            while onceki_sayac_degeri < 0:
                print('Hatali giris.')
                onceki_sayac_degeri = int(input('Lutfen onceki sayac degerini tekrar giriniz::'))
            simdiki_sayac_degeri = int(input('Simdiki sayac degerini giriniz::'))
            while simdiki_sayac_degeri < onceki_sayac_degeri:
                print('Hatali giris.')
                simdiki_sayac_degeri = int(input('Lutfen simdiki sayac degerini tekrar giriniz::'))
            donemlik_su_tuketimi = simdiki_sayac_degeri - onceki_sayac_degeri
            sayac_okunmada_gun_araligi = int(input('Sayacinizin kac gun aralikla okundugunu giriniz::'))
            while sayac_okunmada_gun_araligi < 1:
                sayac_okunmada_gun_araligi = int(input('''Hatali giris.Lutfen 0'dan buyuk bir deger giriniz::'''))

            aylik_sinirlari_donemlik_sinirlara_cevirme_carpani = sayac_okunmada_gun_araligi / 30
            donemlik_1_inci_kademe_siniri = KONUT_TIPI_1_INCI_KADEME_SINIRI * aylik_sinirlari_donemlik_sinirlara_cevirme_carpani
            donemlik_2_inci_kademe_siniri = KONUT_TIPI_2_INCI_KADEME_SINIRI * aylik_sinirlari_donemlik_sinirlara_cevirme_carpani
            hane_basi_ortalama_tuketim=donemlik_su_tuketimi/hane_sayisi
            indirimsiz_hane_sayisi=hane_sayisi-engelli_sayisi-sehit_gazi_sporcu_sayisi
            if 0<=hane_basi_ortalama_tuketim<=donemlik_1_inci_kademe_siniri:
                hane_kademe_1 += hane_sayisi
                hane_kademe_1_aylik_su_tuketimi += donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi #dönemi aylığa çevirme.

                indirimsiz_haneler_su_ucreti=hane_basi_ortalama_tuketim*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI*indirimsiz_hane_sayisi
                indirimsiz_haneler_atik_su_ucreti=hane_basi_ortalama_tuketim*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI*indirimsiz_hane_sayisi

                engelli_indirimli_haneler_su_ucreti=hane_basi_ortalama_tuketim*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI*engelli_sayisi*YIRMI_TONA_KADAR_ENGELLI_INDIRIMI
                engelli_indirimli_haneler_atik_su_ucreti=hane_basi_ortalama_tuketim*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI*engelli_sayisi*YIRMI_TONA_KADAR_ENGELLI_INDIRIMI

                sehit_gazi_sporcu_indirimli_haneler_su_ucreti=hane_basi_ortalama_tuketim*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI*sehit_gazi_sporcu_sayisi*SEHIT_GAZI_SPORCU_INDIRIMI
                sehit_gazi_sporcu_indirimli_haneler_atik_su_ucreti=hane_basi_ortalama_tuketim*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI*sehit_gazi_sporcu_sayisi*SEHIT_GAZI_SPORCU_INDIRIMI

                donemlik_su_tuketim_ucreti=indirimsiz_haneler_su_ucreti+engelli_indirimli_haneler_su_ucreti+sehit_gazi_sporcu_indirimli_haneler_su_ucreti
                donemlik_atik_su_ucreti=indirimsiz_haneler_atik_su_ucreti+engelli_indirimli_haneler_atik_su_ucreti+sehit_gazi_sporcu_indirimli_haneler_atik_su_ucreti
            elif donemlik_1_inci_kademe_siniri<hane_basi_ortalama_tuketim<=donemlik_2_inci_kademe_siniri:
                hane_kademe_2 += hane_sayisi
                hane_kademe_2_aylik_su_tuketimi += donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi #dönemi aylığa çevirme.
                ikinci_kademeye_kalan_su_miktari=hane_basi_ortalama_tuketim-donemlik_1_inci_kademe_siniri

                indirimsiz_haneler_su_ucreti=donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI*indirimsiz_hane_sayisi+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI*indirimsiz_hane_sayisi
                indirimsiz_haneler_atik_su_ucreti=donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI*indirimsiz_hane_sayisi+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI*indirimsiz_hane_sayisi

                engelli_indirimli_haneler_su_ucreti=(donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI*engelli_sayisi+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI*engelli_sayisi)*YIRMI_TONA_KADAR_ENGELLI_INDIRIMI
                engelli_indirimli_haneler_atik_su_ucreti=(donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI*engelli_sayisi+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI*engelli_sayisi)*YIRMI_TONA_KADAR_ENGELLI_INDIRIMI

                sehit_gazi_sporcu_indirimli_haneler_su_ucreti=(donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI*sehit_gazi_sporcu_sayisi+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI*sehit_gazi_sporcu_sayisi)*SEHIT_GAZI_SPORCU_INDIRIMI
                sehit_gazi_sporcu_indirimli_haneler_atik_su_ucreti=(donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI*sehit_gazi_sporcu_sayisi+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI*sehit_gazi_sporcu_sayisi)*SEHIT_GAZI_SPORCU_INDIRIMI

                donemlik_su_tuketim_ucreti=indirimsiz_haneler_su_ucreti+engelli_indirimli_haneler_su_ucreti+sehit_gazi_sporcu_indirimli_haneler_su_ucreti
                donemlik_atik_su_ucreti = indirimsiz_haneler_atik_su_ucreti + engelli_indirimli_haneler_atik_su_ucreti + sehit_gazi_sporcu_indirimli_haneler_atik_su_ucreti
            else:
                hane_kademe_3 += hane_sayisi
                hane_kademe_3_aylik_su_tuketimi += donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi #dönemi aylığa çevirme.
                ucuncu_kademeye_kalan_su_miktari=hane_basi_ortalama_tuketim-donemlik_2_inci_kademe_siniri
                ikinci_kademeye_kalan_su_miktari=hane_basi_ortalama_tuketim-ucuncu_kademeye_kalan_su_miktari-donemlik_1_inci_kademe_siniri

                indirimsiz_haneler_su_ucreti=(donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI+ucuncu_kademeye_kalan_su_miktari*KONUT_TIPI_3_UNCU_KADEME_SU_TUKETIM_BIRIM_UCRETI)*indirimsiz_hane_sayisi
                indirimsiz_haneler_atik_su_ucreti=(donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI+ucuncu_kademeye_kalan_su_miktari*KONUT_TIPI_3_UNCU_KADEME_ATIK_SU_BIRIM_UCRETI)*indirimsiz_hane_sayisi

                engelli_indirimli_haneler_su_ucreti=((donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI)*YIRMI_TONA_KADAR_ENGELLI_INDIRIMI+ucuncu_kademeye_kalan_su_miktari*KONUT_TIPI_3_UNCU_KADEME_SU_TUKETIM_BIRIM_UCRETI)*engelli_sayisi
                engelli_indirimli_haneler_atik_su_ucreti=((donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI)*YIRMI_TONA_KADAR_ENGELLI_INDIRIMI+ucuncu_kademeye_kalan_su_miktari*KONUT_TIPI_3_UNCU_KADEME_ATIK_SU_BIRIM_UCRETI)*engelli_sayisi

                sehit_gazi_sporcu_indirimli_haneler_su_ucreti=(donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETI+ucuncu_kademeye_kalan_su_miktari*KONUT_TIPI_3_UNCU_KADEME_SU_TUKETIM_BIRIM_UCRETI)*sehit_gazi_sporcu_sayisi*SEHIT_GAZI_SPORCU_INDIRIMI
                sehit_gazi_sporcu_indirimli_haneler_atik_su_ucreti=(donemlik_1_inci_kademe_siniri*KONUT_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI+ikinci_kademeye_kalan_su_miktari*KONUT_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI+ucuncu_kademeye_kalan_su_miktari*KONUT_TIPI_3_UNCU_KADEME_ATIK_SU_BIRIM_UCRETI)*sehit_gazi_sporcu_sayisi*SEHIT_GAZI_SPORCU_INDIRIMI

                donemlik_su_tuketim_ucreti = indirimsiz_haneler_su_ucreti + engelli_indirimli_haneler_su_ucreti + sehit_gazi_sporcu_indirimli_haneler_su_ucreti
                donemlik_atik_su_ucreti = indirimsiz_haneler_atik_su_ucreti + engelli_indirimli_haneler_atik_su_ucreti + sehit_gazi_sporcu_indirimli_haneler_atik_su_ucreti

            hane_aylik_tuketim_cevirmesi = donemlik_su_tuketimi * 30 / sayac_okunmada_gun_araligi
            hane_aylik_su_tuketim_toplami += hane_aylik_tuketim_cevirmesi





    elif abone_tipi==2:
        toplu_hane_carpani=1
        isyeri_tipi_abone_sayisi+=1
        abone_tipi_adi='İsyeri tipi abone'

        onceki_sayac_degeri = int(input('Onceki sayac degerini giriniz::'))
        while onceki_sayac_degeri < 0:
            print('Hatali giris.')
            onceki_sayac_degeri = int(input('Lutfen onceki sayac degerini tekrar giriniz::'))
        simdiki_sayac_degeri = int(input('Simdiki sayac degerini giriniz::'))
        while simdiki_sayac_degeri < onceki_sayac_degeri:
            print('Hatali giris.')
            simdiki_sayac_degeri = int(input('Lutfen simdiki sayac degerini tekrar giriniz::'))
        donemlik_su_tuketimi = simdiki_sayac_degeri - onceki_sayac_degeri
        sayac_okunmada_gun_araligi = int(input('Sayacinizin kac gun aralikla okundugunu giriniz::'))
        while sayac_okunmada_gun_araligi < 1:
            sayac_okunmada_gun_araligi = int(input('''Hatali giris.Lutfen 0'dan buyuk bir deger giriniz::'''))

        donemlik_su_tuketim_ucreti=donemlik_su_tuketimi*ISYERI_TIPI_SU_TUKETIM_BIRIM_UCRETI
        donemlik_atik_su_ucreti=donemlik_su_tuketimi*ISYERI_TIPI_ATIK_SU_BIRIM_UCRETI

        isyeri_aylik_su_cevirmesi=donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi
        isyeri_aylik_su_tuketim_toplami+=isyeri_aylik_su_cevirmesi




    elif abone_tipi==3:
        toplu_hane_carpani=1
        resmi_daire_tipi_abone_sayisi+=1
        abone_tipi_adi='Resmi daire tipi abone'

        abone_tipi_adi='Resmi daire tipi abone'
        onceki_sayac_degeri = int(input('Onceki sayac degerini giriniz::'))
        while onceki_sayac_degeri < 0:
            print('Hatali giris.')
            onceki_sayac_degeri = int(input('Lutfen onceki sayac degerini tekrar giriniz::'))
        simdiki_sayac_degeri = int(input('Simdiki sayac degerini giriniz::'))
        while simdiki_sayac_degeri < onceki_sayac_degeri:
            print('Hatali giris.')
            simdiki_sayac_degeri = int(input('Lutfen simdiki sayac degerini tekrar giriniz::'))
        donemlik_su_tuketimi = simdiki_sayac_degeri - onceki_sayac_degeri

        sayac_okunmada_gun_araligi = int(input('Sayacinizin kac gun aralikla okundugunu giriniz::'))
        while sayac_okunmada_gun_araligi < 1:
            sayac_okunmada_gun_araligi = int(input('''Hatali giris.Lutfen 0'dan buyuk bir deger giriniz::'''))


        donemlik_su_tuketim_ucreti=donemlik_su_tuketimi*RESMI_DAIRE_TIPI_SU_TUKETIM_BIRIM_UCRETI
        donemlik_atik_su_ucreti=donemlik_su_tuketimi*RESMI_DAIRE_TIPI_ATIK_SU_BIRIM_UCRETI


        resmi_daire_aylik_su_cevirmesi=donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi
        resmi_daire_aylik_su_tuketim_toplami+=resmi_daire_aylik_su_cevirmesi

        if resmi_daire_max_su_tuketimi<resmi_daire_aylik_su_cevirmesi:
            resmi_daire_max_su_tuketimi=resmi_daire_aylik_su_cevirmesi
            resmi_daire_max_su_tuketen_abone_no=abone_no






    elif abone_tipi==4:
        toplu_hane_carpani=1
        organize_sanayi_tipi_abone_sayisi+=1
        abone_tipi_adi='Organize sanayi tipi abone'

        abone_tipi_adi='Organize sanayi tipi abone'
        onceki_sayac_degeri = int(input('Onceki sayac degerini giriniz::'))
        while onceki_sayac_degeri < 0:
            print('Hatali giris.')
            onceki_sayac_degeri = int(input('Lutfen onceki sayac degerini tekrar giriniz::'))
        simdiki_sayac_degeri = int(input('Simdiki sayac degerini giriniz::'))
        while simdiki_sayac_degeri < onceki_sayac_degeri:
            print('Hatali giris.')
            simdiki_sayac_degeri = int(input('Lutfen simdiki sayac degerini tekrar giriniz::'))
        donemlik_su_tuketimi = simdiki_sayac_degeri - onceki_sayac_degeri
        sayac_okunmada_gun_araligi = int(input('Sayacinizin kac gun aralikla okundugunu giriniz::'))
        while sayac_okunmada_gun_araligi < 1:
            sayac_okunmada_gun_araligi = int(input('''Hatali giris.Lutfen 0'dan buyuk bir deger giriniz::'''))



        donemlik_su_tuketim_ucreti=donemlik_su_tuketimi*ORGANIZE_SANAYI_TIPI_SU_TUKETIM_BIRIM_UCRETI
        donemlik_atik_su_ucreti=donemlik_su_tuketimi*ORGANIZE_SANAYI_TIPI_ATIK_SU_BIRIM_UCRETI

        organize_sanayi_aylik_su_cevirmesi=donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi
        organize_sanayi_aylik_su_tuketim_toplami+=organize_sanayi_aylik_su_cevirmesi



    elif abone_tipi==5:
        toplu_hane_carpani=1
        ilce_tarimsal_ve_hayvansal_sulama_tipi_abone_sayisi+=1
        abone_tipi_adi='Ilce tarimsal ve hayvansal sulama tipi abone'
        onceki_sayac_degeri = int(input('Onceki sayac degerini giriniz::'))
        while onceki_sayac_degeri < 0:
            print('Hatali giris.')
            onceki_sayac_degeri = int(input('Lutfen onceki sayac degerini tekrar giriniz::'))
        simdiki_sayac_degeri = int(input('Simdiki sayac degerini giriniz::'))
        while simdiki_sayac_degeri < onceki_sayac_degeri:
            print('Hatali giris.')
            simdiki_sayac_degeri = int(input('Lutfen simdiki sayac degerini tekrar giriniz::'))
        donemlik_su_tuketimi = simdiki_sayac_degeri - onceki_sayac_degeri
        sayac_okunmada_gun_araligi = int(input('Sayacinizin kac gun aralikla okundugunu giriniz::'))
        while sayac_okunmada_gun_araligi < 1:
            sayac_okunmada_gun_araligi = int(input('''Hatali giris.Lutfen 0'dan buyuk bir deger giriniz::'''))

        aylik_sinirlari_donemlik_sinirlara_cevirme_carpani = sayac_okunmada_gun_araligi/ 30
        donemlik_1_inci_kademe_siniri=ILCE_TARIMSAL_1_INCI_KADEME_SINIRI*aylik_sinirlari_donemlik_sinirlara_cevirme_carpani
        donemlik_2_inci_kademe_siniri=ILCE_TARIMSAL_2_INCI_KADEME_SINIRI*aylik_sinirlari_donemlik_sinirlara_cevirme_carpani
        ilce_tarimsal_ve_hayvansal_aylik_su_tuketimi=donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi

        if ilce_tarimsal_ve_hayvansal_aylik_su_tuketimi>50:
            elli_tondan_fazla_su_tuketen_ilce_tarimsal_hayvansal+=1


        if 0 <= donemlik_su_tuketimi <= donemlik_1_inci_kademe_siniri:
            donemlik_su_tuketim_ucreti = donemlik_su_tuketimi *ILCE_TARIMSAL_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETİ
            donemlik_atik_su_ucreti = donemlik_su_tuketimi *ILCE_TARIMSAL_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI
        elif donemlik_1_inci_kademe_siniri < donemlik_su_tuketimi <= donemlik_2_inci_kademe_siniri:
            ikinci_kademeye_kalan_su_miktari = donemlik_su_tuketimi - donemlik_1_inci_kademe_siniri
            donemlik_su_tuketim_ucreti = donemlik_1_inci_kademe_siniri *ILCE_TARIMSAL_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETİ + ikinci_kademeye_kalan_su_miktari *ILCE_TARIMSAL_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETİ
            donemlik_atik_su_ucreti = donemlik_1_inci_kademe_siniri *ILCE_TARIMSAL_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI + ikinci_kademeye_kalan_su_miktari *ILCE_TARIMSAL_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI
        else:
            ucuncu_kademeye_kalan_su_miktari = donemlik_su_tuketimi - donemlik_2_inci_kademe_siniri
            ikinci_kademeye_kalan_su_miktari = donemlik_su_tuketimi - ucuncu_kademeye_kalan_su_miktari - donemlik_1_inci_kademe_siniri

            donemlik_su_tuketim_ucreti = donemlik_1_inci_kademe_siniri *ILCE_TARIMSAL_TIPI_1_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETİ+ ikinci_kademeye_kalan_su_miktari *ILCE_TARIMSAL_TIPI_2_INCI_KADEME_SU_TUKETIM_BIRIM_UCRETİ + ucuncu_kademeye_kalan_su_miktari *ILCE_TARIMSAL_TIPI_3_UNCU_KADEME_SU_TUKETIM_BIRIM_UCRETİ
            donemlik_atik_su_ucreti = donemlik_1_inci_kademe_siniri *ILCE_TARIMSAL_TIPI_1_INCI_KADEME_ATIK_SU_BIRIM_UCRETI + ikinci_kademeye_kalan_su_miktari *ILCE_TARIMSAL_TIPI_2_INCI_KADEME_ATIK_SU_BIRIM_UCRETI + ucuncu_kademeye_kalan_su_miktari *ILCE_TARIMSAL_TIPI3_UNCU_KADEME_ATIK_SU_BIRIM_UCRETI

        ilce_tarimsal_ve_hayvansal_aylik_su_cevirmesi = donemlik_su_tuketimi * 30 / sayac_okunmada_gun_araligi
        ilce_tarimsal_ve_hayvansal_aylik_su_tuketim_toplami+=ilce_tarimsal_ve_hayvansal_aylik_su_cevirmesi




    donemlik_su_vergili_tuketim_ucreti = donemlik_su_tuketim_ucreti+donemlik_su_tuketim_ucreti *KDV
    donemlik_atik_su_vergili_ucreti =donemlik_atik_su_ucreti + donemlik_atik_su_ucreti * KDV
    donemlik_vergisiz_su_ve_atik_su_ucreti=donemlik_su_tuketim_ucreti+donemlik_atik_su_ucreti
    donemlik_vergili_toplam_atik_su_ve_su_ucret = donemlik_su_vergili_tuketim_ucreti + donemlik_atik_su_vergili_ucreti
    donemlik_ctv_tutari =donemlik_su_tuketimi * TON_BASINA_CTV
    donemlik_vergili_kati_atik_toplama_ucreti =(HANE_BASI_KATI_ATIK_TOPLAMA_UCRETİ + HANE_BASI_KATI_ATIK_TOPLAMA_UCRETİ * KDV)*toplu_hane_carpani
    donemlik_vergili_kati_atik_bertaraf_ucreti = (HANE_BASI_KATI_ATIK_BERTARAF_UCRETİ + HANE_BASI_KATI_ATIK_BERTARAF_UCRETİ * KDV)*toplu_hane_carpani
    toplam_fatura_tutari =donemlik_vergili_toplam_atik_su_ve_su_ucret + donemlik_ctv_tutari + donemlik_vergili_kati_atik_toplama_ucreti + donemlik_vergili_kati_atik_bertaraf_ucreti
    devlete_aktarilacak_toplam_kdv =(donemlik_vergisiz_su_ve_atik_su_ucreti+(HANE_BASI_KATI_ATIK_TOPLAMA_UCRETİ+HANE_BASI_KATI_ATIK_BERTARAF_UCRETİ)*toplu_hane_carpani)*KDV   #CTV den KDV alınmıyor.
    ilce_belediyesine_aktarilacak_tutar = donemlik_ctv_tutari + HANE_BASI_KATI_ATIK_TOPLAMA_UCRETİ*toplu_hane_carpani  # Donemliğe çevrilmeden alınabileceği söylenmişti.
    buyuksehir_belediyesine_aktarilacak_tutar =HANE_BASI_KATI_ATIK_BERTARAF_UCRETİ*toplu_hane_carpani  # Dönemliğe çevrilmeden alınabileceği söylenmişti.
    donemlik_izsu_payi =donemlik_su_tuketim_ucreti + donemlik_atik_su_ucreti

    if  abone_tipi!=1 and  max_tuketim_yapan_konut_disi_abonenin_ucreti<toplam_fatura_tutari*30/sayac_okunmada_gun_araligi:     #Dönemlik aylığa çevrildi.
        max_tuketim_yapan_konut_disi_abonenin_ucreti=toplam_fatura_tutari*30/sayac_okunmada_gun_araligi     #Dönemlik aylığa çevrildi.
        max_tuketim_yapan_abonenin_nosu=abone_no
        max_tuketim_yapan_abonenin_abonelik_tipi=abone_tipi_adi
        max_tuketim_yapan_abonenin_aylik_su_tuketimi=donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi     #Dönemlik aylığa çevrildi.



    print('Abone numaranız::',abone_no)
    print('Abone tipi adiniz::',abone_tipi_adi)
    print('Donemlik su tuketim miktari::',donemlik_su_tuketimi,'ton')
    print('Donemlik su tuketim ucreti::',format(donemlik_su_tuketim_ucreti,'.2f'),'TL')
    print('Donemlik atık su ucreti::',format(donemlik_atik_su_ucreti,'.2f'),'TL')
    print('Donemlik toplam su tuketim ve atik su ucreti::',format(donemlik_vergisiz_su_ve_atik_su_ucreti,'.2f'),'TL')
    print('Donemlik CTV tutari::',format(donemlik_ctv_tutari,'.2f'),'TL')
    print('Donemlik kati atik toplama ucreti::',HANE_BASI_KATI_ATIK_TOPLAMA_UCRETİ*toplu_hane_carpani,'TL')
    print('Donemlik kati atik bertaraf ucreti::',HANE_BASI_KATI_ATIK_BERTARAF_UCRETİ*toplu_hane_carpani,'TL')
    print('Donemlik toplam fatura bedeli::',format(toplam_fatura_tutari,'.2f'),'TL')
    print('Donemlik devlete aktarilacak toplam KDV::',format(devlete_aktarilacak_toplam_kdv,'.2f'),'TL')
    print('Donemlik ilce belediyesine aktarilacak tutar::',format(ilce_belediyesine_aktarilacak_tutar,'.2f'),'TL')
    print('Donemlik buyuksehir belediyesine aktarilacak tutar::',format(buyuksehir_belediyesine_aktarilacak_tutar,'.2f'),'TL')
    print('Donemlik IZSU payi::',format(donemlik_izsu_payi,'.2f'),'TL')
    toplam_izsu_payi+=donemlik_izsu_payi
    toplam_ilce_belediyesi_payi+=ilce_belediyesine_aktarilacak_tutar
    toplam_buyuksehir_belediyesi_payi+=buyuksehir_belediyesine_aktarilacak_tutar
    toplam_devlet_payi+=devlete_aktarilacak_toplam_kdv



    aylik_su_tuketimi=donemlik_su_tuketimi*30/sayac_okunmada_gun_araligi
    aylik_ucret=toplam_fatura_tutari*30/sayac_okunmada_gun_araligi

    if abone_tipi==1:
        hane_aylik_su_tuketim_ucreti+=aylik_ucret
    elif abone_tipi==2:
        isyeri_aylik_su_tuketim_ucreti+=aylik_ucret
    elif abone_tipi==3:
        resmi_daire_aylik_su_tuketim_ucreti+=aylik_ucret
    elif abone_tipi==4:
        organize_sanayi_aylik_su_tuketim_ucreti+=aylik_ucret
    else:
        ilce_tarimsal_ve_hayvansal_sulama_su_tuketim_ucreti+aylik_ucret


    if (aylik_su_tuketimi>100 or aylik_ucret>500) and not(hane_sayisi>0):   #konut dışı için hesaplama.
        cok_su_tuketen_aboneler+=1
    if hane_sayisi>0 and (hane_basi_ortalama_tuketim>100 or aylik_ucret/hane_sayisi>500):  #konut tipi için hesaplama.
        cok_su_tuketen_aboneler+=hane_sayisi

    devam=input('Devam etmek icin E/e, cikis icin H/h tuslayiniz::')
    while  not(devam=='h' or devam=='H' or devam=='E' or devam=='e'):
        print('Hatali devam girisi.Lutfen E/e veya H/h tuslayiniz')
        devam=input()

if devam=='h' or devam=='H':
    print('')
    print('Abone girisinlerini tamamladiniz.İstatistikler asagida olusturuldu.')


toplam_abone_sayisi=hane_tipi_abone_sayisi+isyeri_tipi_abone_sayisi+resmi_daire_tipi_abone_sayisi+organize_sanayi_tipi_abone_sayisi+ilce_tarimsal_ve_hayvansal_sulama_tipi_abone_sayisi

print('Hane tipi abone sayisi::',hane_tipi_abone_sayisi,'Toplam abone icindeki yuzdesi::%',format(hane_tipi_abone_sayisi*100/toplam_abone_sayisi,'.2f'))
if hane_tipi_abone_sayisi>0:
    print('Hane tipi abonelerin aylik ortalama su tuketim miktari::',format(hane_aylik_su_tuketim_toplami/hane_tipi_abone_sayisi,'.2f'),'ton')
else:
    print('Hane tipi abonelerin aylik ortalama su tuketim miktari::0 ton')

print('Isyeri tipi abone sayisi::',isyeri_tipi_abone_sayisi,'Toplam abone icindeki yuzdesi::%',format(isyeri_tipi_abone_sayisi*100/toplam_abone_sayisi,'.2f'))
if isyeri_tipi_abone_sayisi>0:
    print('Isyeri tipi abonelerin aylik ortalama su tuketim miktari::',format(isyeri_aylik_su_tuketim_toplami/isyeri_tipi_abone_sayisi,'.2f'),'ton')
else:
    print('Isyeri tipi abonelerin aylik ortalama su tuketim miktari::0 ton')

print('Resmi daire tipi abone sayisi::',resmi_daire_tipi_abone_sayisi,'Toplam abone icindeki yuzdesi::%',format(resmi_daire_tipi_abone_sayisi*100/toplam_abone_sayisi,'.2f'))
if resmi_daire_tipi_abone_sayisi>0:
    print('Resmi daire tipi abonelerin aylik ortalama su tuketim miktari::',format(resmi_daire_aylik_su_tuketim_toplami/resmi_daire_tipi_abone_sayisi,'.2f'),'ton')
else:
    print('Resmi daire tipi abonelerin aylik ortalama su tuketim miktari::0')

print('Organize sanayi tipi abone sayisi::',organize_sanayi_tipi_abone_sayisi,'Toplam abone icindeki yuzdesi::%',format(organize_sanayi_tipi_abone_sayisi*100/toplam_abone_sayisi,'.2f'))
if organize_sanayi_tipi_abone_sayisi>0:
    print('Organize sanayi tipi abonelerin aylik ortalama su tuketim miktari::',format(organize_sanayi_aylik_su_tuketim_toplami/organize_sanayi_tipi_abone_sayisi,'.2f'),'ton')
else:
    print('Organize sanayi tipi abonelerin aylik ortalama su tuketim miktari::0 ton')

print('Ilce tarimsal ve hayvansal tipi abone sayisi',ilce_tarimsal_ve_hayvansal_sulama_tipi_abone_sayisi,'Toplam abone icindeki yuzdesi::%',format(ilce_tarimsal_ve_hayvansal_sulama_tipi_abone_sayisi*100/toplam_abone_sayisi,'.2f'))
if ilce_tarimsal_ve_hayvansal_sulama_tipi_abone_sayisi>0:
    print('Ilce tarimsal ve hayvansal tipi abonelerin aylik ortalama su tuketimi::',format(ilce_tarimsal_ve_hayvansal_aylik_su_tuketim_toplami/ilce_tarimsal_ve_hayvansal_sulama_tipi_abone_sayisi,'.2f'),'ton')
else:
    print('Ilce tarimsal ve hayvansal tipi abonelerin aylik ortalama su tuketimi::0')

if hane_tipi_abone_sayisi>0:
    print('1 inci kademede su tuketen konutlarin sayisi::',hane_kademe_1,'Tum konutlar icindeki yuzdeleri::%',format(hane_kademe_1*100/hane_tipi_abone_sayisi,'.2f'))
    print('2 inci kademede su tuketen konutlarin sayisi::', hane_kademe_2, 'Tum konutlar icindeki yuzdeleri::%',format(hane_kademe_2 * 100 / hane_tipi_abone_sayisi, '.2f'))
    print('3 uncu kademede su tuketen konutlarin sayisi::', hane_kademe_3, 'Tum konutlar icindeki yuzdeleri::%',format(hane_kademe_3 * 100 / hane_tipi_abone_sayisi, '.2f'))
if hane_kademe_1>0:
    print('1 inci kademede su tuketen konutlarin ortalama su tuketimi::',format(hane_kademe_1_aylik_su_tuketimi/hane_kademe_1,'.2f'),'ton')
if hane_kademe_2>0:
    print('2 inci kademede su tuketen konutlarin ortalama su tuketimi::',format(hane_kademe_2_aylik_su_tuketimi/hane_kademe_2,'.2f'),'ton')
if hane_kademe_3>0:
    print('3 uncu kademede su tuketen konutlarin ortalama su tuketimi::',format(hane_kademe_3_aylik_su_tuketimi/hane_kademe_3,'.2f'),'ton')

print('Aylik su tuketimi 50 tondan fazla olan ilce tarimsal ve hayvansal sulama tipi abonelerin sayisi::',elli_tondan_fazla_su_tuketen_ilce_tarimsal_hayvansal)
if ilce_tarimsal_ve_hayvansal_sulama_tipi_abone_sayisi>0:
    print('Aylik su tuketimi 50 tondan fazla olan ilce tarimsal ve hayvansal sulama tipi abonelerin tum ilce tarimsal ve hayvansalda yuzdesi::%',format(elli_tondan_fazla_su_tuketen_ilce_tarimsal_hayvansal*100/ilce_tarimsal_ve_hayvansal_sulama_tipi_abone_sayisi,'.2f'))

print('Aylik su tuketim miktari 100 tondan yuksek veya aylik faturasi 500 TL den fazla olan abone sayisi::',cok_su_tuketen_aboneler)

if hane_tipi_abone_sayisi>0:
    print('Sehit yakini,gazi,sporcu ve engelli abonelerin toplam sayisi::',indirimli_abone_sayisi,'toplam konut tipi icinde yuzdeleri::%',format(indirimli_abone_sayisi*100/hane_tipi_abone_sayisi,'.2f'))
else:
    print('Sehit yakini,gazi,sporcu ve engelli abonelerin toplam sayisi::0')

if resmi_daire_max_su_tuketimi>0:
    print('En fazla su tuketen resmi dairenin abone nosu::',resmi_daire_max_su_tuketen_abone_no,'Tukettigi su miktari::',resmi_daire_max_su_tuketimi,'ton')
else:
    print('Resmi daire tipi abone girisi yapilmamis!')

if max_tuketim_yapan_abonenin_nosu>0:  #Konut dışı maximum tüketim.
    print('En fazla tuketim yapan konut disi abonenin nosu::',max_tuketim_yapan_abonenin_nosu,'Abone tipi::',max_tuketim_yapan_abonenin_abonelik_tipi)
    print('Bu abonenin aylık su tuketim miktari::',max_tuketim_yapan_abonenin_aylik_su_tuketimi,'ton','Odedigi_ucret::',format(max_tuketim_yapan_konut_disi_abonenin_ucreti,'.2f'),'TL')

bornovanin_su_tuketim_toplami=hane_aylik_su_tuketim_toplami+isyeri_aylik_su_tuketim_toplami+resmi_daire_aylik_su_tuketim_toplami+organize_sanayi_aylik_su_tuketim_toplami+ilce_tarimsal_ve_hayvansal_aylik_su_tuketim_toplami
print('Hane tipi abonelerin aylik toplam su tuketim miktari::',format(hane_aylik_su_tuketim_toplami,'.2f'),'ton','Bornova icindeki yuzdesi::%',format(hane_aylik_su_tuketim_toplami*100/bornovanin_su_tuketim_toplami,'.2f'))
print('Isyeri tipi abonelerin aylik toplam su tuketim miktari::',format(isyeri_aylik_su_tuketim_toplami,'.2f'),'ton','Bornova icindeki yuzdesi::%',format(isyeri_aylik_su_tuketim_toplami*100/bornovanin_su_tuketim_toplami,'.2f'))
print('Resmi daire tipi abonelerin aylik toplam su tuketim miktari::',format(resmi_daire_aylik_su_tuketim_toplami,'.2f'),'ton','Bornova icindeki yuzdesi::%',format(resmi_daire_aylik_su_tuketim_toplami*100/bornovanin_su_tuketim_toplami,'.2f'))
print('Organize sanayi tipi abonelerin aylik toplam su tuketim miktari::',format(organize_sanayi_aylik_su_tuketim_toplami,'.2f'),'ton','Bornova icindeki yuzdesi::%',format(organize_sanayi_aylik_su_tuketim_toplami*100/bornovanin_su_tuketim_toplami,'.2f'))
print('Ilce tarimsal ve hayvan sulama tipi abonelerin aylik toplam su tuketim miktari::',format(ilce_tarimsal_ve_hayvansal_aylik_su_tuketim_toplami,'.2f'),'ton','Bornova icindeki yuzdesi::%',format(ilce_tarimsal_ve_hayvansal_aylik_su_tuketim_toplami*100/bornovanin_su_tuketim_toplami,'.2f'))
print('Bornovanin aylik toplam su tuketimi::',format(bornovanin_su_tuketim_toplami,'.2f'),'ton')

tum_abonelerden_elde_edilen_aylik_su_tuketim_tutari=hane_aylik_su_tuketim_ucreti+isyeri_aylik_su_tuketim_ucreti+resmi_daire_aylik_su_tuketim_ucreti+organize_sanayi_aylik_su_tuketim_ucreti+ilce_tarimsal_ve_hayvansal_sulama_su_tuketim_ucreti
print('Hane tipi abonelerin aylik toplam su tuketim ucreti::',format(hane_aylik_su_tuketim_ucreti,'.2f'),'TL')
print('Isyeri tipi abonelerin aylik toplam su tuketim ucreti::',format(isyeri_aylik_su_tuketim_ucreti,'.2f'),'TL')
print('Resmi daire tipi abonelerin aylik toplam su tuketim ucreti::',format(resmi_daire_aylik_su_tuketim_ucreti,'.2f'),'TL')
print('Organize sanayi tipi abonelerin aylik toplam su tuketim ucreti::',format(organize_sanayi_aylik_su_tuketim_ucreti,'.2f'),'TL')
print('Ilce tarimsal ve hayvan sulama tipi abonelerin aylik toplam su tuketim ucreti::',format(ilce_tarimsal_ve_hayvansal_sulama_su_tuketim_ucreti,'.2f'),'TL')
print('Bornovanin aylik toplam su tuketim ucreti::',format(tum_abonelerden_elde_edilen_aylik_su_tuketim_tutari,'.2f'),'TL')

print('Donemde IZSU nun elde ettigi toplam gelir::',format(toplam_izsu_payi,'.2f'),'TL')
print('Donemde ilce belediyesinin elde ettigi toplam gelir::',format(toplam_ilce_belediyesi_payi,'.2f'),'TL')
print('Donemde buyuksehir belediyesinin elde ettigi toplam gelir::',format(toplam_buyuksehir_belediyesi_payi,'.2f'),'TL')
print('Donemde devletin elde ettigi toplam gelir::',format(toplam_devlet_payi,'.2f'),'TL')

end=input()

