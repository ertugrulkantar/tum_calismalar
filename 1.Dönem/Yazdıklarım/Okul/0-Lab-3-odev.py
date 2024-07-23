oyuncu_numarasi=int(input('Oyuncunun numarasini giriniz::'))
normal_sezon_mac_sayisi=int(input('Oyuncunun normal sezondaki mac sayisi::'))
normal_sezon_sayi=int(input('Oyuncunun normal sezondaki toplam sayisi::'))
normal_sezon_asist=int(input('Oyuncunun normal sezondaki asist sayisi::'))
normal_sezon_ribaund=int(input('Oyuncunun normal sezondaki ribaund sayisi::'))

takim_playoffta_mi=input('Oyuncunun takimi playoffta mi(E/H)::')

if oyuncu_numarasi==1:
    oyuncu_mevki='Oyun Kurucu'
elif oyuncu_numarasi==2:
    oyuncu_mevki='Sutor Guard'
elif oyuncu_numarasi==3:
    oyuncu_mevki='Kisa Forvet'
elif oyuncu_numarasi==4:
    oyuncu_mevki='Uzun Forvet'
elif oyuncu_numarasi==5:
    oyuncu_mevki='Pivot'
else:
    oyuncu_mevki='hatali girildi!!!'

if takim_playoffta_mi=='E':
    playoff_mac_sayisi=int(input('Oyuncunun playofftaki mac sayisi::'))
    playoff_sayi=int(input('Oyuncunun playofftaki toplam sayisi:: '))
    playoff_asist=int(input('Oyuncunun playofftaki toplam asisti::'))
    playoff_ribaund=int(input('Oyuncunun playofftaki toplam ribaundu::'))
else:
    playoff_mac_sayisi=0
    playoff_sayi=0
    playoff_asist=0
    playoff_ribaund=0

toplam_mac_sayisi=normal_sezon_mac_sayisi+playoff_mac_sayisi
toplam_sayi=normal_sezon_sayi+playoff_sayi
toplam_asist=normal_sezon_asist+playoff_asist
toplam_ribaund=normal_sezon_ribaund+playoff_ribaund

ortalama_sayi=round(toplam_sayi/toplam_mac_sayisi,2)
ortalama_asist=round(toplam_asist/toplam_mac_sayisi,2)
ortalama_ribaund=round(toplam_ribaund/toplam_mac_sayisi,2)


print('Oyuncunun oynadıgı mevki',oyuncu_mevki)
print('Oyuncunun sezondaki toplam mac sayisi:',toplam_mac_sayisi)
print('Oyuncunun sezondaki mac basi ortalama skoru:',ortalama_sayi)
print('Oyuncunun sezondaki mac basi ortalama ribaundu:',ortalama_ribaund)
print('Oyuncunun sezondaki mac basi ortalama asist sayisi:',ortalama_asist)

end=input()