BİRİM_SAAT_UCRETİ=33.45
HAFTALİK_NORMAL_CALİSMA_SURESİ=40
haftalik_calisma=int(input('haftalik calisma saatini giriniz:'))
if haftalik_calisma>HAFTALİK_NORMAL_CALİSMA_SURESİ:
    haftalik_ekstra_calisma=haftalik_calisma-HAFTALİK_NORMAL_CALİSMA_SURESİ
    ekstra_ucret=haftalik_ekstra_calisma*BİRİM_SAAT_UCRETİ*1.5
    toplam_ucret=(HAFTALİK_NORMAL_CALİSMA_SURESİ)*BİRİM_SAAT_UCRETİ+ekstra_ucret
    print('toplam ucret::',toplam_ucret)
else:
    toplam_ucret2=haftalik_calisma*BİRİM_SAAT_UCRETİ
    print('toplam ucret::',toplam_ucret2)
end=input('end')