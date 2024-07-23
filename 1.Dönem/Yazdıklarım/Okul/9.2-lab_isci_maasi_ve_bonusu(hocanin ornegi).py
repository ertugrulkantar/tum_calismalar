BİRİM_SAAT_UCRETİ=33.45
HAFTALİK_NORMAL_CALİSMA_SURESİ=40
calisma_suresi=int(input('haftalik calisma suresini giriniz::'))
ek_ucret=0
if calisma_suresi>HAFTALİK_NORMAL_CALİSMA_SURESİ:
    ek_ucret=(calisma_suresi-HAFTALİK_NORMAL_CALİSMA_SURESİ)*BİRİM_SAAT_UCRETİ/2
#burada ek ücret hesaplanırken 0.5 ile çarpılmış. daha sonra total ücret
#hesaplanırken ek ücreti 1.5 çarpani ile hesaplamak yerine calisma süresini
#direkt birim saat ücreti çarpanı ile hesaplamış.
#yani ekstra ücreti 1.5 ile çarparkenki 1/1 lik kısmı
#alınmış. Daha sonra ek_ucretteki 1/2(0.5) lik kısmı da
#ilave edilmiş.
#baya değişik bir yol.
ucret=calisma_suresi*BİRİM_SAAT_UCRETİ+ek_ucret
print('Ondenecek Ucret::',format(ucret,'.2f'))
end=input('end')
