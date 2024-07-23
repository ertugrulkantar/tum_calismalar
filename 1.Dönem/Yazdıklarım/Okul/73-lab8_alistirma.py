def main():
    standart_sapma_payi=0
    ortalamadan_yuksek_ogrenciler=0
    ogrencilerin_not_listesi=[]
    giris='E'
    while giris=='E' or giris=='e':
        ogrenci_notu=int(input('Ogrencinin notunu giriniz::'))
        ogrencilerin_not_listesi.append(ogrenci_notu)
        giris=input('Baska ogrenci girmek ister misiniz(E/e/H/h)::')
    ogrencilerin_not_toplami=sum(ogrencilerin_not_listesi)
    not_ortalamasi=ogrencilerin_not_toplami/len(ogrencilerin_not_listesi)
    for eleman in ogrencilerin_not_listesi:
        standart_sapma_payi+=(eleman-not_ortalamasi)**2
    try:
        standart_sapma=(standart_sapma_payi/(len(ogrencilerin_not_listesi)-1))**(1/2)   #Öğrenci sayısı 1 ise zerodivision fırlatır.
    except ZeroDivisionError:
        print('Tek ogrenci icin standart sapma hesaplanamaz!')
    for eleman in ogrencilerin_not_listesi:
        if eleman>not_ortalamasi:
            ortalamadan_yuksek_ogrenciler+=1
    en_yuksek_not=max(ogrencilerin_not_listesi)
    en_dusuk_not=min(ogrencilerin_not_listesi)
    print('Sinifin not ortalamasi=',format(not_ortalamasi,'.2f'),sep='')
    print('Sinifin standart sapmasi=',format(standart_sapma,'.2f'),sep='')
    print('Notu sinif not ortalamasindan yuksek olan ogrenci sayisi=',ortalamadan_yuksek_ogrenciler,'Siniftaki yuzdeleri=',format(ortalamadan_yuksek_ogrenciler*100/len(ogrencilerin_not_listesi),'.2f'))
    print('Max not=',en_yuksek_not)
    print('Min not=',en_dusuk_not)

main()