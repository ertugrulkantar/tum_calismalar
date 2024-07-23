#Bu program yağmur verilerini işler.Lab'da yapıldı.
#for örneği.line 20 sonrası sıkıntılı düzelt.

bugun_kacinci_gun=int(input('Bugun_ayin_kacinci_gunu::'))
yagmurlu_gun_sayisi=0
yagmursuz_gun_sayisi=0
yagmur_kac_kg_toplam=0

for gun_no in range(1,bugun_kacinci_gun+1,1):    #sondaki 1 argümanı gereksiz.
    print('Ayin',gun_no,'. gunu yagmurlu mu?')
    yagmurlu_mu=input('(E/H)')
    if yagmurlu_mu=='E':
        yagmur_kac_kg=int(input('Metrekareye kac kg yagis dustu::'))
        yagmur_kac_kg_toplam+=yagmur_kac_kg
        yagmurlu_gun_sayisi+=1
    else:
        yagmursuz_gun_sayisi+=1

print('Yagmurlu gun sayisi:',yagmurlu_gun_sayisi)
print('Yagmurlu gun yuzdesi:',round(yagmurlu_gun_sayisi*100/bugun_kacinci_gun,2))

if yagmurlu_gun_sayisi!=0:
    print('Gunluk ortalama yagis miktari(kg):',round(yagmur_kac_kg_toplam/bugun_kacinci_gun,2))
else:
    print('Hic yagmur yagmadi.')

end=input()