
adi_ve_soyadi=input('oyuncu_adi_ve_soyadini_giriniz::')

sezon_toplam_mac=int(input('oyuncunun_bu_sezonki_toplam_mac_sayisi::'))

serbest_toplam=int(input('oyuncunun_attigi_toplam_serbest_atis_sayisi::'))
serbest_basarili=int(input('oyuncunun_attigi_toplam_basarili_serbest_atis_sayisi::'))
serbest_basarisiz=int(input('oyuncunun_attigi_toplam_basarisiz_serbest_atis_sayisi::'))

ikilik_toplam=int(input('oyuncunun_attigi_toplam_ikilik_sayisi::'))
ikilik_basarili=int(input('oyuncunun_attigi_toplam_basarili_ikilik_sayisi::'))
ikilik_basarisiz=int(input('oyuncunun_attigi_toplam_basarisiz_ikilik_sayisi::'))

ucluk_toplam=int(input('oyuncunun_attigi_toplam_ucluk_sayisi::'))
ucluk_basarili=int(input('oyuncunun_attigi_toplam_basarili_ucluk_sayisi::'))
ucluk_basarisiz=int(input('oyuncunun_attigi_toplam_basarisiz_ucluk_sayisi::'))

toplam_sayi=serbest_basarili+(2*ikilik_basarili)+(3*ucluk_basarili)

mac_basi_ortalama=format(toplam_sayi/sezon_toplam_mac,'.2f')

serbest_yuzde=float(((serbest_toplam-serbest_basarisiz)/serbest_toplam)*100)
ikilik_yuzde=float(((ikilik_toplam-ikilik_basarisiz)/ikilik_toplam)*100)
ucluk_yuzde=float(((ucluk_toplam-ucluk_basarisiz)/ucluk_toplam)*100)

print(adi_ve_soyadi,'adli_oyuncunun_bilgi_ve_istatistikleri::')
print('oyuncunun_attigi_toplam_sayi::',toplam_sayi)
print('oyuncunun_mac_basi_ortalama_sayisi::',mac_basi_ortalama)
print('oyuncunun_serbest_atis_yuzdesi::',format(serbest_yuzde,'.2f'))
print('oyuncunun_ikilik_yuzdesi',format(ikilik_yuzde,'.2f'))
print('oyuncunun_ucluk_yuzdesi',format(ucluk_yuzde,'.2f'))
end=input('son')