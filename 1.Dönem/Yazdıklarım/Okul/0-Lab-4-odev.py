toplam_oyun_suresi=0
toplam_skor=0
toplam_mac_sayisi=0
ilk_beste_basladigi_maclar=0
ilk_beste_baslayip_sayi_atamadigi_maclar=0
kenardan_basladigi_maclar=0
ilk_beste_basladigi_maclardaki_toplam_skoru=0
kenarda_basladigi_maclardaki_toplam_skoru=0
verimli_oyun=0
ilk_beste_basladigi_maclardaki_toplam_suresi=0
kenardan_basladigi_maclardaki_toplam_oyunda_kalma_suresi=0

oyun_suresi=int(input('Oyuncu bu macinda kac dakika oyunda kaldi::'))

while oyun_suresi!=0:
    toplam_mac_sayisi+=1
    print('Oyuncu maca ilk beste mi yoksa kenardan mi basladi?')
    baslangic_pozisyonu=input('b/k::')
    if baslangic_pozisyonu=='b':
        ilk_beste_basladigi_maclar+=1
        ilk_beste_basladigi_macta_oyunda_kalma_suresi=oyun_suresi
        ilk_beste_basladigi_maclardaki_toplam_suresi+=ilk_beste_basladigi_macta_oyunda_kalma_suresi
        ilk_beste_basladigi_macta_attigi_sayi=int(input('Oyuncu oyunda kac sayi atti::'))
        ilk_beste_basladigi_maclardaki_toplam_skoru+=ilk_beste_basladigi_macta_attigi_sayi
        toplam_skor+=ilk_beste_basladigi_macta_attigi_sayi
        if ilk_beste_basladigi_macta_attigi_sayi==0:
            ilk_beste_baslayip_sayi_atamadigi_maclar+=1
        if ilk_beste_basladigi_macta_attigi_sayi/oyun_suresi>=1:
            verimli_oyun+=1
        bu_mactaki_verimlilik=round(ilk_beste_basladigi_macta_attigi_sayi/ilk_beste_basladigi_macta_oyunda_kalma_suresi,2)
        print('Oyuncunun bu mactaki verimliligi:',bu_mactaki_verimlilik)
    elif baslangic_pozisyonu=='k':
        kenardan_basladigi_maclar+=1
        kenardan_basladigi_macta_oyunda_kalma_suresi=oyun_suresi
        kenardan_basladigi_maclardaki_toplam_oyunda_kalma_suresi+=kenardan_basladigi_macta_oyunda_kalma_suresi
        kenardan_basladigi_macta_attigi_sayi=int(input('Oyuncu oyunda kac sayi atti::'))
        kenarda_basladigi_maclardaki_toplam_skoru+=kenardan_basladigi_macta_attigi_sayi
        toplam_skor+=kenardan_basladigi_macta_attigi_sayi
        bu_mactaki_verimlilik=round(kenardan_basladigi_macta_attigi_sayi/kenardan_basladigi_macta_oyunda_kalma_suresi,2)
        print('Oyuncunun bu mactaki verimliligi:',bu_mactaki_verimlilik)
        if kenardan_basladigi_macta_attigi_sayi/oyun_suresi>=1:
            verimli_oyun+=1
    print('Oyuncu siradaki gireceginiz oyunda kac dakika kaldi?')
    oyun_suresi=int(input('Devam etmek icin oyun suresini,cikis icin 0 veya negatif bir sayiyi giriniz::'))

ilk_beste_basladigi_maclarin_yuzdesi=round(ilk_beste_basladigi_maclar*100/toplam_mac_sayisi,2)
ilk_bes_basladigi_maclarda_oyunda_kaldigi_ortalama_sure=round(ilk_beste_basladigi_maclardaki_toplam_suresi/ilk_beste_basladigi_maclar,2)
ilk_beste_basladigi_maclarda_ortalama_attigi_sayi=round(ilk_beste_basladigi_maclardaki_toplam_skoru/ilk_beste_basladigi_maclar,2)
kenarda_basladigi_maclarin_yuzdesi=round(kenardan_basladigi_maclar*100/toplam_mac_sayisi,2)
kenarda_basladigi_maclarda_oyunda_kaldigi_ortalama_sure=round(kenardan_basladigi_maclardaki_toplam_oyunda_kalma_suresi/kenardan_basladigi_maclar,2)
kenarda_basladigi_maclarda_ortalama_attigi_sayi=round(kenarda_basladigi_maclardaki_toplam_skoru/kenardan_basladigi_maclar,2)
tum_maclarda_oyunda_kaldigi_toplam_sure=ilk_beste_basladigi_maclardaki_toplam_suresi+kenardan_basladigi_maclardaki_toplam_oyunda_kalma_suresi
tum_maclarda_oyunda_kaldigi_ortalama_sure=round(tum_maclarda_oyunda_kaldigi_toplam_sure/toplam_mac_sayisi,2)
tum_maclardaki_mac_basi_ortalama_sayisi=round(toplam_skor/toplam_mac_sayisi,2)
ilk_beste_baslayip_hic_sayi_atamadigi_mac_yuzdesi=round(ilk_beste_baslayip_sayi_atamadigi_maclar*100/ilk_beste_basladigi_maclar,2)

print('Oyuncunun ilk beste basladigi mac sayisi::',ilk_beste_basladigi_maclar,'yuzdesi::%',ilk_beste_basladigi_maclarin_yuzdesi)
print('Oyuncunun kenarda basladigi mac sayisi::',kenardan_basladigi_maclar,'yuzdesi::%',kenarda_basladigi_maclarin_yuzdesi)
print('Oyuncunun ilk beste basladigi maclardaki ortalama oyunda kalma suresi::',ilk_bes_basladigi_maclarda_oyunda_kaldigi_ortalama_sure,'dakikadır')
print('Oyuncunun ilk beste basladigi maclardaki ortalama mac basi sayisi::',ilk_beste_basladigi_maclarda_ortalama_attigi_sayi)
print('Kenardan basladigi maclarda ortalama oyunda kalma suresi::',kenarda_basladigi_maclarda_oyunda_kaldigi_ortalama_sure,'dakikadir')
print('Kenardan basladigi maclardaki ortalama mac basi sayisi::',kenarda_basladigi_maclarda_ortalama_attigi_sayi)
print('Oyuncunun tum maclar icin mac basina ortalama olarak oynadigi sure::',tum_maclarda_oyunda_kaldigi_ortalama_sure,'dakikadir')
print('Oyuncunun tum maclar icin mac basina ortalama attigi sayi::',tum_maclardaki_mac_basi_ortalama_sayisi)
print('Oyuncunun verimliliginin 1 veya uzeri oldugu mac sayisi::',verimli_oyun)
print('Oyuncunun ilk beste baslayip hic sayi atamadigi maclarin ilk beste basladigi maclara oranla yuzdesi::%',ilk_beste_baslayip_hic_sayi_atamadigi_mac_yuzdesi)

end=input()