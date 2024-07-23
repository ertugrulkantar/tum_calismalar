simdiki_saat=int(input('saati giriniz'))
simdiki_dakika=int(input('dakikayi giriniz'))
kac_saattir_arabadasin=int(input('kac saattir arabadasiniz'))
kac_dakikadir_arabadasin=int(input('kac dakikadir arabadasin'))
gece_yarisindan_beri_gecen_dakika=simdiki_saat*60+simdiki_dakika
arabada_gecen_dakika=kac_dakikadir_arabadasin*60+kac_dakikadir_arabadasin
arabaya_binis_ani=gece_yarisindan_beri_gecen_dakika-arabada_gecen_dakika
su_anki_saat=(arabaya_binis_ani//60)%24
su_anki_dakika=arabaya_binis_ani%60
print('arabaya bindiginiz saat::',su_anki_saat,':',su_anki_dakika)
gg=input('end')