#Baya güzel bir örnek.
#Kullanıcıdan sayısı bilinmeyen kız ve erkek öğrencilerin
#notlarını alıp daha sonra kız-erkek ayrı ve birleşik
#sınavla ilgii çıktıları veren bir program.

notu=int(input('1.ogrencinin notunu giriniz::'))
erkek_ogrenci_notu=0
basarili_erkek=0
basarisiz_erkek=0

kiz_ogrenci_notu=0
basarili_kiz=0
basarisiz_kiz=0

while 100>=notu>=0:
    ogrenci_cinsiyeti = input('Ogrenci cinsiyeti(E/K)')
    if ogrenci_cinsiyeti=='E':
        erkek_ogrenci_notu+=notu
        if notu>=60:
            basarili_erkek+=1
        else:
            basarisiz_erkek+=1
    elif ogrenci_cinsiyeti=='K':
        kiz_ogrenci_notu+=notu
        if notu>=60:
            basarili_kiz+=1
        else:
            basarisiz_kiz+=1
    notu=int(input('Diger notu giriniz veya cikis icin 111 yaziniz.'))

toplam_erkek=basarili_erkek+basarisiz_erkek
toplam_kiz=basarisiz_kiz+basarili_kiz
toplam_basarili=basarili_kiz+basarili_erkek
toplam_basarisiz=basarisiz_kiz+basarisiz_erkek
toplam_ogrenci=toplam_erkek+toplam_kiz
toplam_not=erkek_ogrenci_notu+kiz_ogrenci_notu

sinif_not_ortalamasi=round(toplam_not/toplam_ogrenci,2)

if toplam_basarili!=0:
    basarili_ogrenci_orani=round(toplam_basarili*100/toplam_ogrenci,2)

if toplam_erkek!=0:
    basarili_erkek_orani=round(basarili_erkek*100/toplam_erkek,2)
    basarisiz_erkek_orani=round(basarisiz_erkek*100/toplam_erkek,2)

if toplam_kiz!=0:
    basarili_kiz_orani=round(basarili_kiz*100/toplam_kiz,2)
    basarisiz_kiz_orani=round(basarisiz_kiz*100/toplam_kiz,2)

print('Sinifin not ortalamasi:',sinif_not_ortalamasi,sep='')
print('Sinifin basari orani:%',basarili_ogrenci_orani,sep='')
print('Basarili erkek ortani:%',basarili_erkek_orani,sep='')
print('Basarisiz erkek orani:%',basarisiz_erkek_orani,sep='')
print('Basarili kiz orani:%',basarili_kiz_orani,sep='')
print('Basarisiz kiz orani:%',basarisiz_kiz_orani,sep='')

end=input()