import random
def ornek1():
    list1=list('ali')
    print(list1)
    list2=list(range(5))    #range 0,1,2,3,4 üretir.
    print(list2)

def repetation_ornek2():
    list1=[1,2,3,5]
    list2=list1*3   #Repetation işareti,yani yıldız,sağda olmalı.
    print(list2)

def index_ornek3():
    list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for index in range(10,15):
        print(list1[index])
    for index in range(-11,-6):
        print(list1[index])     #Düz
    for index in range(-6,-11,-1):
        print(list1[index])     #Ters

def len_ornek4():
    '''Liste eleman sayısını verir.'''
    list1=[1,2,3,4]*4
    eleman_say=len(list1)   #exception handler olarak kullanılabiliyor
    print(eleman_say)       #bu fonksiyon.

def kapsamli_ornek5():
    ort_ustu_abone_say=0     #Abonelerin verilerini ayrı ayrı tutup
    top_tuketim=0            #daha sonra ort üstü aboneleri ve toplamı
    ABONE_SAY=10             #bulan program.
    tuketimler=[0]*ABONE_SAY
    for i in range(ABONE_SAY):
        print(i+1,'. abone aylik tuketimi::')
        tuketimler[i]=int(input('::'))
        top_tuketim+=tuketimler[i]
    ort_tuketim=top_tuketim/ABONE_SAY
    for tuketim in tuketimler:
        if tuketim>ort_tuketim:
            ort_ustu_abone_say+=1
    print(ort_ustu_abone_say)

def liste_birlestirme_ornek6():
    list1=[1,2,3]
    list2=[4,5,6]
    list3=list1+list2
    print(list3)

def slicing_ornek7():
    list1=[1,2,3,4,5,6,7,8,9,10]
    list2=list1[2:6]       #End değeri dahil değil.
    print('list2',list2)
    list3=list1[:6]     #Startı 0 varsayar.
    print('list3',list3)
    list4=list1[2:]     #Endi sona kadar alır.
    print('list4',list4)
    list5=list1[:]      #Hepsini alır.
    print('list5',list5)
    list6=list1[2:6:2]   #Step seçilebilir.
    print('list6',list6)
    list7=list1[-5:2]   #Boş liste döndürür.
    print('list7',list7)
    list8=list1[-5:-2]
    print('list8',list8)
    list1[2:6]=[1,2,3,4]
    print('list1',list1)

def index_metodu_ornek8():
    '''Index metodu yakaladığı ilk itemin indexini döndürür.Yakalamazsa exception'''
    '''Çalıştırırken try/except bloğu kullanılmalı.'''
    list1=[1,2,3,3,4]
    print(list1.index(3))

def insert_metodu_ornek9():
    '''Araya eleman ekler.'''
    list1=[0,1,2,3,4,5,6]
    list1.insert(4,444)
    print(list1)

def sort_metodu_ornek10():
    '''Sıralar.'''
    list1=[7,6,22,3,4,5,-1,-99]
    list1.sort()
    print(list1)
    list1.sort(reverse=True)   #Tersten sıralama
    print(list1)

def remove_metodu_ornek11():
    '''İtemi bulup siler.Bulamazsa exception'''
    list1=[1,2,3,4,5,99]
    list1.remove(99)
    print(list1)

def reverse_metodu_ornek12():
    '''O anki sıralamayı tersine çevirir.'''
    list1=[123,33,42,7,66]
    list1.reverse()
    print(list1)

def extend_metodu_ornek13():
    '''extend metodu listeyi ekler.'+' işareti ile aynı işleve sahip.'''
    list1=[1,2,3]
    list2=[4,5,6]
    list1=list1+list2
    print('+ ile',list1)
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1.extend(list2)
    print('extend ile',list1)

def pop_metodu_ornek14():
    '''Verilen indexteki elemanı siler.'''
    list1=[0,1,2,3,4,5,6,7]
    list1.pop(3)
    print(list1)

def count_metodu_ornek15():
    '''Verilen itemden kaç tane olduğunu sayar.'''
    list1=[1,2,3,3,3,4,5,6]
    print(list1.count(3))

def del_fonksiyonu_ile_pop_metodu_farki_ornek16():
    '''del fonksiyonunda aralık girebilirsin;pop metodunda giremezsin.'''
    list1=[0,1,2,3,4,5,6,7]
    del list1[3:6]
    print(list1)

def sum_fonksiyonu_ornek17():
    '''Liste elemanlarını toplar.'''
    list1=[25,50,75,100]
    toplam=sum(list1)
    print(toplam)

def sorted_fonksiyonu_ornek18():
    '''Fonksiyon olduğundan asıl listeyi bozmadan sıralama yapabilirsin.'''
    list1=[99,-22,33,12,1,3,88]
    list2=sorted(list1)
    print(list2)

def listenin_kopyasını_olusturma_ornek19():
    '''= ile bu işi yapamazsın.Adresler aynı itemi gösterir;birinin indexinde'''
    '''yaptığın değişiklik diğerine etki eder.'''
    '''Ama yeni bir liste oluşturursan etki etmez.'''
    '''a=b assigmenti sorun yaratmazken;listede yaratabilir.'''
    #= ile deneme:
    list1=[0,1,2,3,4]
    list2=list1
    list2[0]=10
    print('= ile list1:',list1)
    print('Yani eşittir ile kopya oluşturulamıyor.')
    print('4 kopya yolu::')
    #4 kopya yolu var.
    #1-for döngüsü ile
    print('---1---')
    list1=[0,1,2,3,4]
    list2=[]
    for el in list1:
        list2.append(el)
    print('list2 for ile',list2)
    #2-copy metodu ile
    print('---2---')
    list1=[-1,-2,-3,-4]
    list2=list1.copy()
    print('list2 copy ile',list2)
    #3-boş liste ile:
    print('---3---')
    list1=[10,20,30,40]
    list2=[]+list1
    print('list2 bos liste ile',list2)
    #4-slicing ile
    print('---4---')
    list1=[77,88,99,100]
    list2=list1[:]      #Yani slicing yapıldığında yeni liste oluşturulur.
    print('list2 slicing ile',list2)

def tavla_zari_ornek20():
    '''Index programa entegre edilebilir olduğundan kullanılabiliyor.'''
    tekrar_say=[0]*6   #tavladaki her zar için 0 oluşturuldu.
    for i in range(1000):   #zar 1000 defa atılıyor.
        yuzu=random.randrange(1,7)  #random ile atıldı.
        tekrar_say[yuzu-1]+=1   #yuzu ile tekrar kümesi entegre edildi.
    print(tekrar_say)

def hafta_10_son_ornek21():
    '''Bir şirketin 10 elemanı var.Bir ay 30 gün.'''
    '''Her gün için satıcıların satışları belli.'''
    '''Bunlar programa girildikten sonra istenen'''
    '''bu satıcıların ay sonunda ne kadar satış yaptığı.'''
    satici_toplamlari=[0]*10
    for gun in range(30):
        for satici_no in range(10):
            satis_tutari=random.randrange(0,100)    #Bu problemde de index programa
            satici_toplamlari[satici_no]+=satis_tutari  #dahil edilebiliyor.
    print('--1-----2-----3-----4-----5-----6-----7-----8-----9-----10')
    print(satici_toplamlari)

def gaddis_chap7_ornek22():
    '''-in- operatörü kullanımı'''
    list1=['Ertugrul','Ahmet','Mehmet']
    ad=input('Adini gir::')
    if ad in list1:
        print('Adin listede.')

def string_de_listedir_ornek23():
    ad='Ertugrul'
    print(ad.index('g'))

def liste_karsilastirmmasi_ornek24():
    '''Liste elemanlarını karşılaştırır'''
    '''ilk farklılığa göre karar verir.'''
    list1=[1,2,3,4,5,6,7]
    list2=[1,2,3,4,5,6,8]
    if list2>list1:
        print('True')

def metot_deger_dondurmez_ornek25():
    my_list=[4,7,1,2]
    my_list=my_list.sort()
    print('Metot ile atama',my_list)
    list2=[4,7,1,2]
    list2.sort()
    print('Metot ile dogru yol',list2)
    '''Fonksiyon döndürür.'''
    list1=[4,7,1,2]
    list1=sorted(list1)
    print('Fonksiyon ile',list1)

def slicing_detay_ornek26():
    list=9*[0]         #Eğer başlangıç indexi(pozitif olanı)
    print(list)        #bitiş indexinden büyükse slicing
    print(list[-5:8])  #boş liste döndürür.

def append_detay_ornek27():
    list1=[1,2,3,4,4]
    list1.append(5)     #Tek argüman alır.
    print(list1)
    list1.append(list1) #Sonsuz döngü.Çünkü eklerken aynı zamanda kendi sonuna da ekliyor.
    print(list1)
