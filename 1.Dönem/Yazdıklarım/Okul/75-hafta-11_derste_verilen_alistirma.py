#Hafta-11 alıştırma.
#Öğrenci numarası ve not(0-100) alınacak.Öğrenci numarasına bir not girildikten sonra
#o öğrenciye bir daha not girilmesi engellenecek.
#İstenen:(0-10)(10-20).. aralığındaki öğrenci sayısı.Döngü E/H ile kurulacak.
def main1():
    ogrenci_no_list=[]
    ogrenci_not_list=[]

    devam='E'
    while devam in ['E','e']:
        ogrenci_no=int(input('Ogrenci numarasini giriniz::'))
        while ogrenci_no in ogrenci_no_list:
            ogrenci_no=int(input('Ogrenci numarasi mevcut!Lütfen yeni numara giriniz::'))
        ogrenci_notu = int(input('Ogrencinin notunu giriniz::'))
        ogrenci_no_list.append(ogrenci_no)
        ogrenci_not_list.append(ogrenci_notu)
        devam=input('Devam için E/e,bitirmek için H/h giriniz::')

    aralik1,aralik2,aralik3,aralik4,aralik5,aralik6,aralik7,aralik8,aralik9,aralik10=0,0,0,0,0,0,0,0,0,0
    for eleman in ogrenci_not_list:
        if eleman<11:
            aralik1+=1
        elif eleman<21:
            aralik2+=1
        elif eleman<31:
            aralik3+=1
        elif eleman<41:
            aralik4+=1
        elif eleman<51:
            aralik5+=1
        elif eleman<61:
            aralik6+=1
        elif eleman<71:
            aralik7+=1
        elif eleman<81:
            aralik8+=1
        elif eleman<91:
            aralik9+=1
        else:
            aralik10+=1

    print('Not Araligi      ',end='')
    print('Sayi')
    print('----------      ------')
    print('  0-10           ',aralik1)
    print('  11-20          ',aralik2)
    print('  21-30          ',aralik3)
    print('  31-40          ',aralik4)
    print('  41-50          ',aralik5)
    print('  51-60          ',aralik6)
    print('  61-70          ',aralik7)
    print('  71-80          ',aralik8)
    print('  61-90          ',aralik9)
    print('  91-100         ',aralik10)

main1()