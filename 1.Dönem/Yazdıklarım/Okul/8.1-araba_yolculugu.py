simdiki_saat=int(input('saati giriniz'))
simdiki_dakika=int(input('dakikayi giriniz'))
kac_saattir_araba_kullaniyor=int(input('kac saattir araba kullaniyorsunuz?'))
kac_dakikadir_araba_kullaniyor=int(input('kac dakikadir araba kullaniyorsunuz?'))
yola_ciktigi_dakika=simdiki_dakika-kac_dakikadir_araba_kullaniyor
yola_ciktigi_saat=simdiki_saat-kac_saattir_araba_kullaniyor
if yola_ciktigi_dakika<0:
    yola_ciktigi_dakika=yola_ciktigi_dakika+60
    yola_ciktigi_saat=yola_ciktigi_saat-1
if yola_ciktigi_saat<0:
    yola_ciktigi_saat=yola_ciktigi_saat+24
print('yola ciktiginiz saat::',yola_ciktigi_saat,':',yola_ciktigi_dakika)
print('yalnizca elit beyler icin :D')
end=input('end')