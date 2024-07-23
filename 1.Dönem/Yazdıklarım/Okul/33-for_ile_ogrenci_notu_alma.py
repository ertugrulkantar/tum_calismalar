#Bir sınıftaki öğrenci sayısını ve her öğrenci için
#ara sınav ve final notlarını alan ve öğrencilerin dönem sonu
#notu ile başarı durumunu yazdıran program. (arasınav katkısı %40;final katkısı %60)

ogr_sayisi=int(input('Ogrenci sayisini giriniz::'))

for sayac in range(ogr_sayisi):
    print(sayac+1,'. ogrencinin notlarini girin:',sep='')
    arasinav=int(input('Ara sinav notu::'))
    final=int(input('Final notu::'))
    donem_sonu=(arasinav*0.4+final*0.6)
    print('Donem sonu notu=',donem_sonu,sep='')
    if donem_sonu>=60:
        print(sayac+1,'nolu ogrenci gecti')
    else:
        print(sayac+1,'nolu ogrenci kaldi.')

end=input()