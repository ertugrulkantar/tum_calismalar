MAX_BOY=175
MIN_KILO=75
boy_toplam=kilo_toplam=0
kazanan_say=0
devam='e'

while devam=='E' or devam=='e':
    ad_soyad=input('Asker adayinin adi ve soyadi::')
    kilo=int(input('Asker adayinin kilosu::'))
    boy=int(input('Asker adayinin boyu::'))
    if boy>=175 and kilo<=75:
        print('Askersin!!!')
        boy_toplam+=boy
        kilo_toplam+=kilo
        kazanan_say+=1
        if boy>=MAX_BOY:
            MAX_BOY=boy
            max_boy_ad_soyad=ad_soyad
        if kilo<=MIN_KILO:
            MIN_KILO=kilo
            min_kilo_ad_soyad=ad_soyad
    else:
        print('Kazanamadin :(')
    devam=input('Baska aday var mi?(E/e)-(H/h)::')

print('Askerlerin boy ortalamasi',boy_toplam/kazanan_say,sep='=')
print('Askerlerin kilo ortalamasi',kilo_toplam/kazanan_say,sep='=')
print('En uzun asker::',max_boy_ad_soyad,'boyu::',MAX_BOY)
print('En zayif asker::',min_kilo_ad_soyad,'kilosu::',MIN_KILO)

end=input()

