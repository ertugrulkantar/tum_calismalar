#Hafta 11 alıştırma.
#10 satıcı(1-10) her biri için gün gün satış verisi giriliyor.Bir hafta boyunca veriler
#biriktiriliyor.Girilenler:Gün numarası,satıcı numarası,satış miktarı.
#İstenenler:Tabloyu printle,satıcıların satış toplamları,günlerdeki toplam satış.

satislar=[]

for satici_no in range(10):
    bir_satici=[0]*7
    satislar.append(bir_satici)

devam='E'
while devam in ['E','e']:
    gun_no=int(input('Gun numarasini giriniz::'))
    satici_no=int(input('Satici numarasini giriniz::'))
    satis_miktari=int(input('Satis miktarini giriniz::'))
    satislar[satici_no][gun_no]=satis_miktari
    devam=input('Devam için E/e,cikis icin H/h tuslayiniz::')

gun_toplam=[0]*7    #Sütunları toplamak için.Satırlarda aşağıdaki gibi kısa yoldan halledilebiliyor.

for satici_no in range(10):     #Tabloyu printliyoruz.
    for gun_no in range(7):
        gun_toplam[gun_no]+=satislar[satici_no][gun_no]
        print(satislar[satici_no][gun_no])
    print(sum(satislar[satici_no]))     #Direkt o satırı(yani o satıcının satışlarını) toplar.
                                        #Bunun yerine bu satıra 10'luk bir satıcı no listesiyle
for gun_no in range(7):                 #satici_list[satici_no]+=sum(gun_toplam) yapılabilir.
    print(gun_toplam[gun_no])

print(sum(gun_toplam))
