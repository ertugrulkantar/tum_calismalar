SABİT_BURS=100
NOT_ORTALAMASİ_BURS_CARPANİ=25
ad_soyad=input('adiniz ve soyadiniz:')
not_ortalamasi=float(input('not ortalamaniz='))
cinsiyet=input('cinsiyetiniz e/k:')

if cinsiyet=='k':
    aile_geliri=float(input('ailenizin gelirini giriniz:'))
else:
    aile=geliri=0
if cinsiyet=='k' and aile_geliri<1700:
    kiz_bursu=100
else:
    kiz_bursu=0
if not_ortalamasi>=2.00:
    not_ortalamasi_bursu=not_ortalamasi*NOT_ORTALAMASİ_BURS_CARPANİ
total_burs=SABİT_BURS+not_ortalamasi_bursu+kiz_bursu
print('Sayin',ad_soyad,'toplam alacaginiz burs::',total_burs)
end=input('end')
