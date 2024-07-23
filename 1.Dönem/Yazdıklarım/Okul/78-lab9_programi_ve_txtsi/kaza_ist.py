# Problem:
# Türkiye’de meydana gelen trafik kazalarının nedenleri araştırılmış ve en çok görülen
# sürücü kaynaklı kaza nedenleri 1’den başlayarak aşağıdaki şekilde kodlandırılmıştır.
# 
# Sürücü Kaynaklı Kaza Nedenleri	Kaza Nedeni Kodu
# Aşırı Hız				1
# Kural İhlali				2
# Dikkatsizlik				3
# Hatalı Sollama			4
# Uykusuzluk				5
# Acemilik				6
# Alkol					7
# Yakın Takip				8
# Agresiflik				9
# Diğer					10
# 
# Sigorta şirketleri bir yıl boyunca meydana gelen her trafik kazasına ilişkin
# il plaka kodu (1-81), kaza nedeni kodu (1-10) ve hasar tutarı verilerini “kazalar.txt”
# isimli bir dosyada biriktirmişlerdir. Dosyanın her satırında yalnız 1 veri elemanı 
# bulunmaktadır (örnek bir veri dosyası ekte verilmiştir). Bu dosyadaki verileri kullanarak,
# Türkiye’de bir yıl içerisinde meydana gelen toplam kaza sayılarının ve bu kazaların
# toplam hasar tutarlarının illere ve kaza nedenlerine göre dağılımını bulan ve 
# aşağıdaki gibi ekranda listeleyen bir program yazınız:
# 
# İllere ve Kaza Nedenlerine Göre Yıllık Kaza Sayıları
# İl Kodu	Aşırı Hız	Kural İhlali	...	...	Diğer		Toplam
# ---------	---------	------------	---	---	-----		------
# ...		...		...		...	...	...		...
# Toplam	...		...		...	...	...		...
# 
# 
# İllere ve Kaza Nedenlerine Göre Yıllık Hasar Tutarları
# İl Kodu	Aşırı Hız	Kural İhlali	...	...	Diğer		Toplam
# ---------	---------	------------	---	---	-----		------
# ...		...		...		...	...	...		...
# Toplam	...		...		...	...	...		...


#Program:
def kaza_verilerini_al_ve_listeleri_olustur(kaza_dosyasi,tum_kaza_sayilari,tum_hasar_tutarlari):
    il_kodu_str=kaza_dosyasi.readline()
    while il_kodu_str!="":
        il_kodu=int(il_kodu_str)
        kaza_nedeni_kodu=int(kaza_dosyasi.readline())
        hasar_tutari=int(kaza_dosyasi.readline())
        tum_kaza_sayilari[il_kodu-1][kaza_nedeni_kodu-1]+=1
        tum_hasar_tutarlari[il_kodu - 1][kaza_nedeni_kodu - 1] += hasar_tutari
        il_kodu_str=kaza_dosyasi.readline()

def tablo_yazdir(iki_boyutlu_liste):
    print("İl Kodu ",end="")
    for kaza_nedeni_kodu in range(1,11):
        print(format(kaza_nedenleri[kaza_nedeni_kodu],"13"),end="")
    print("Toplam")
    print("------- ",end="")
    for kaza_nedeni_kodu in range(1,11):
        print("------------ ",end="")
    print("------")
    sutun_top=[0]*10
    for il_kodu in range(81):
        print(format(il_kodu+1,"2"),"     ",end="")
        for kaza_nedeni_kodu in range(10):
            print(format(iki_boyutlu_liste[il_kodu][kaza_nedeni_kodu],"6"),"      ",end="")
            sutun_top[kaza_nedeni_kodu]+=iki_boyutlu_liste[il_kodu][kaza_nedeni_kodu]
        print(format(sum(iki_boyutlu_liste[il_kodu]),"6"))
    print("Toplam  ",end="")
    for kaza_nedeni_kodu in range(10):
        print(format(sutun_top[kaza_nedeni_kodu], "6"),"      ", end="")
    print(format(sum(sutun_top),"6"))

try:
    kaza_dosyasi=open("kazalar.txt","r")
    kaza_nedenleri={1:"Aşırı Hız", 2:"Kural İhlali", 3:"Dikkatsizlik", 4:"Sollama", 5:"Uykusuzluk", 6:"Acemilik", 7:"Alkol", 8:"Yakın Takip", 9:"Agresiflik", 10:"Diğer"}
    tum_kaza_sayilari=[]
    tum_hasar_tutarlari=[]
    for il_kodu in range(81):
        bir_ilin_kaza_sayilari=[0]*10
        tum_kaza_sayilari.append(bir_ilin_kaza_sayilari)
        bir_ilin_hasar_tutarlari=[0]*10
        tum_hasar_tutarlari.append(bir_ilin_hasar_tutarlari)

    kaza_verilerini_al_ve_listeleri_olustur(kaza_dosyasi,tum_kaza_sayilari,tum_hasar_tutarlari)
    kaza_dosyasi.close()
except IOError:
    print("Veri dosyası açılamadı ya da okunamadı!")
else:
    print("İllere ve Kaza Nedenlerine Göre Yıllık Kaza Sayıları")
    tablo_yazdir(tum_kaza_sayilari)
    bir_tus=input()
    print("İllere ve Kaza Nedenlerine Göre Yıllık Hasar Tutarları")
    tablo_yazdir(tum_hasar_tutarlari)
