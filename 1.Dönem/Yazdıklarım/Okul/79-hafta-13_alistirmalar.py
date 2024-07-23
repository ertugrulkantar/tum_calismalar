def es_adresleme_ne_zaman_bozulur_ornek1():
    #Index ve slicing kullanarak kısmi değişiklik yapıldığında bozulmaz.
    list_a=[1,2,3]
    list_A=list_a
    list_a[1]=99
    print(list_A)   #bozulmadı
    list_a[0:3]=[0,0,0]
    print(list_A)   #bozulmadı
    #Assigment ile bozulur.
    list_b=[2,2,2]
    list_B=list_b
    list_b=[99,88,77]
    print(list_B)

def slicing_de_sinirlarin_asilmasi_ornek2():
    #Error alınmaz.Liste uyum göstereceği şekilde değişir.
    list1=[0,1,2,3,4,5,6,7,8,9]
    list1[7:13]=['x','x','x','x','x','x']   #Genişler.
    print(list1)
    #2.durum
    list2=[0,1,2,3,4,5,6,7,8,9]
    list2[7:13]=['x']   #Yalnız 7'nci indexe atanma yapıldı.Gerisi ''
    print(list2)

def slicing_de_sinirlarin_ayni_olmasi_ornek3():
    list1=[1,2,3,4,5]
    list2=list1[2:2]
    print(list2)

def hafta13_soru1():
    '''Girilen sözcüğün palindrom(tersiyle düzü aynı şekilde okunabilen*kazak gibi*) olup olmadığını belirleyen program.'''
    str1=input('Sozcugu giriniz::')
    ters_str=str1[::-1]
    if str1==ters_str:
        print('Sozcuk palindrom.')
    else:
        print('Sozcuk palindrom degil.')
    #2.Yol----
    for i in range(len(str1)):
        if str1[i]!=str1[-i-1]:
            print('**Sozcuk palindrom degil.**')
            break
    else:
        print('**Sozcuk palindrom.**')

def hafta13_soru2():
    '''Türkçe harfleri de içeren bir metindeki harflerin tekrar sayılarını bulan program.'''
    '''Büyük-küçük harf duyarlı olmayacak.Sadece Türkçe karakterler;(x,q,w) yok.'''
    def buyuk_harf(harf):
        if harf=='i':
            return 'İ'
        elif harf=='ı':
            return 'I'
        else:
            return harf.upper()

    harf_say=[0]*29
    turkce_alfabe='ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    metin=input('Harfleri sayılacak metni giriniz::')
    for karakter in metin:
        buyuk_kar=buyuk_harf(karakter)
        index=turkce_alfabe.find(buyuk_kar) #Exception vermez,-1 döndürür.
        if index!=-1:
            harf_say[index]+=1
    for i in range(len(turkce_alfabe)):
        print(turkce_alfabe[i],harf_say[i])

def dict_te_get_metodu_ornek4():
    dict1={}
    dict1['ertugrul']=dict1.get('ertugrul',20)  #Yok ise 2.argümana eşitler.
    print(dict1)
    dict1['ertugrul']=dict1.get('ertugrul',9999)+35 #Var ise atanan değeri baz alır.
    print(dict1)

def hizalamada_detay_ornek5():
    '''Hizalamada < ve > ne işe yarar?'''
    list1=[0,1,2,3,4,5,6,7,8]
    list2=['a','b','c','d','e','f','g','h','999999999999']
    for i in range(len(list1)):
        print(format(list1[i],'<10'),end='')
        print(list2[i])

def immutableyi_ne_bozmaz_ornek6():
    #1 Yeniden atama
    tup1=(1,2,3,4,5)
    tup1=(9,8,7,6)
    print(tup1)
    #2 Concatenation
    tup2=(-1,-2,-3)
    tup2+=tup1
    print(tup2)

def string_metotlari_ornek7():
    #1-isalnum()--->Tüm karakterler harf ve sayıdan oluşuyorsa True,başka karakter varsa False.
    print('1------')
    str1='AB CD'
    str2='ABCD'
    print('1-',str1.isalnum())
    print('2-',str2.isalnum())
    print('2------')
    #2-isalpha ve isdigit
    str1='ASDASDASD'
    print('1-',str1.isalpha())
    str2='113322'
    print('2-',str2.isdigit())
    print('3------')
    #3-islower ve isupper
    str1='AAAAA'
    print('1-',str1.isupper())
    print('2-',str2.islower())
    print('4------')
    #4-isspace--->Karakterlerin tümü whitespace(space,\n,\t)ise True döndürür,aksi halde veya karakter yoksa False döndürür.
    str1=''
    print('1-',str1.isspace())
    str1='\n \t   '
    print('2-',str1.isspace())
    print('5------')
    #5-lower ve upper
    str1='abcd'
    str2='KKLM'
    print(str1.upper(),str2.lower())

def string_metotlari2_ornek8():
    print('1------')
    #lstrip,rstrip,strip    #Argümanlı ve argümansız çalışırlar.
    str1='   \n\t A l i'      #Soldaki whitespace'leri siler.
    print(str1.lstrip())
    str1='A l i    \n\t    '  #Sağdaki whitespace'leri siler.
    print(str1.rstrip())
    str1='\n\t  A l i   \t\n' #Soldaki ve sağdaki whitespace'leri siler.
    print(str1.strip())
    str1='AADADAA'   #Hangi karakterlerin silineceği argüman olarak verilebilir.
    print(str1.strip('A'))  #Ama yalnızca baş ve sondakileri sildiğine dikkat et.
    print('2------')
    str1='Aliveli'
    print(str1.endswith('li'))  #Sondan başlayarak karakterlerin varlığını kontrol eder,True-False döndürür.
    print(str1.startswith('Ali'))   #Baştan başlayarak karakterlerin varlığını kontrol eder.True-False döndürür.
    print('3------')
    str1='Aliiii'
    print(str1.find('i'))   #Verilen argümanın str'deki indexini verir.İlk bulduğunu döndürür.
    print(str1.find('z'))   #Bulamazsa exception fırlatmaz,-1 döndürür.
    str1='Erthgrhl'
    print(str1.replace('h','u'))    #str'de mevcut olan ilk argümandaki karakterler yerine ikincisini yerleştirir.
    str1='Nuriye Aliye Cifte Telliye'   #Tek karakter olmak zorunda değil.
    print(str1.replace('ye','e'))
    print('4------')
    str1='AABBCCDDEE-qweqweqweqwe'
    print(str1.split('-'))  #Argüman vermezsen space'lerden,verirsen argümandan ayırır.Ayrım , ile yapılıyor.

def str_metot_ve_fonksiyonları_ornek9():
    print(ord('A')) #Karakterin UTF-8 değerini verir.
    print(chr(65))  #UTF-8 değerine sahip karakteri verir.
    ####
    str1='Aliveli'
    print(str1[::-1])   #Tersten gitmek.
    ####Zincirleme metot kullanımı
    str1='Python Rules Hot'
    print(str1.upper().find('O'))
    ####
    print(str1.find('o',13))   #find metodunun 2'nci argümanı aramanın nereden başlayacağını belirler.
    ####Format'ın metot olarak yeni bir kullanımı
    print('Sorry,is this the {} minute {}?'.format(5,'ARGUMENT'))   #{} yerine verilen argümanları yerleştirir.
    print('{0} is {2} and {0} is also {1}'.format('Bill',25,'tall'))    #Sıraya göre karışık argüman yerleştirilebilir.




