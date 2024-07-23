def dal1():
    '''1-STR FUNC'''
    x=75
    x=str(x)    #Verileni str ye çevirir.
    print('1- x=75; x=str(x); type(x)=',type(x),' #STR KULLANIMI \n',sep="")

def dal2():
    '''2-INT+FLOAT=FLOAT'''
    print('2- 34+6.33=',34+6.33," #INT+FLOAT=FLOAT\n",sep="")

def dal3():
    '''3-PRINTTE INT PARAMETRESI'''
    print('3-','A','B',end='X')
    print('BURAYI BITISTIRIR!!',' #END PARAMETRESI KULLANIMI\n')

def dal4():
    '''4-FORMATLA ILGILI OZET'''
    x=format(0.75,'%')
    print('4.1- x=format(0.75,"%") x=',x,' #FORMAT KULLANIMI',sep="")

    print('4.2- type(x)=',type(x),' #FORMAT STR CIKARIR',sep="")

    x=format(0.35,'.2%')
    print("4.3- format(0.35,'.2%')=",x,' #FORMATTA ONDALIK KULLANIMI',sep="")

    x=format(0.6854,'.2f')
    print("4.4 format(0.6854,'.2f')=",x,' #FORMAT DA YUVARLAMA YAPAR\n',sep="")

def dal5():
    '''5-INT-FLOAT DETAYI'''
    x=42
    print("5-","42::",type(x),"#42 INTTIR")
    y=42.0
    print("42.0::",type(y),"#42.0 FLOATTIR\n")

def dal6():
    '''6-TAM SAYI BOLMESI DETAY'''
    print("6- 5//2=",5//2)
    print("-5//2=",-5//2," #YANI HER TURLU KUCUGE YUVARLAR\n")

def dal7():
    '''7-EXPONENTIATION (US ALMA) DETAY'''
    print("7- 2^3^2!=64 ;","2^3^2=",2**3**2," #BURDA SAGDAN SOLA GIDILIR\n")

def dal8():
    ''' 8-BOOL NE ZAMAN FALSE OLUR'''
    print("8- bool(0)=",bool(0),"  bool("")=",bool("")," #BOOL IFADESI YALNIZ 0 ve "" ARGUMANLARINDA FALSE OLUR.\n",sep="")

def dal9():
    '''9-RANDINT-RANDRANGE FARKI'''
    import random
    print("RANDINT ILE STEP SECILEMEZ::",random.randint(0,10))
    print("RANDRANGE ILE SECILEBILIR::",random.randrange(0,10,2)," #HER ZAMAN CIFT DONDURUR.\n")

def dal10():
    '''10-LOCAL VARIABLEYI GLOBALLESTIRME'''
    def f1():
        global localidimgloballestim
        localidimgloballestim=5
    f1()
    print("10- DEGISKEN GLOBAL ATANDIKTAN SONRA ILGILI FONKSIYON CAGIRILIRSA GLOBAL KULLANILIR,CAGIRILMAZSA\n"
      "ERROR ALINIR. localidimgloballestim=",localidimgloballestim,"\n",sep="")

def dal11():
    '''11-LOCAL DEGISKENLER ICIN KARMASIK BIR KURAL'''
    print("11- NESTED FONKSIYONLARDA LOCAL DEGISKENLER SADECE LOCAL OLDUGU YERDE KULLANILABILIR.\n"
      "ICTEKI DISIN; DISTAKI ICIN LOCALINI KULLANAMAZ.FONKSIYONU INCELE.")
    def g1():
        dista=5
        def g2():
            ##dista+=5  ERROR ALINIR.
            icte=7
            print("#YALNIZCA ICTEKI DISTAKI DEGERI PRINTLEYEBILIR.DEGER=",dista,sep="")    #SADECE PRINT CALISABILIYOR.
        g2()
        ##icte+=5   ERROR ALINIR.
    g1()
    print("\n")

def dal12():
    '''12-LISTE FONKSIYONA GONDERILIRSE'''
    list1=[3,5,7]
    print("12- LISTE FONKSIYONDA DEGISTIRILIRSE DEGISIR. BURADAKI DETAY EGER AYNI ADDA LOCAL BIR LISTE\n"
      "DAHA OLUSTURULURSA O ZAMAN O LISTE KULLANILIR, GLOBAL DEGISMEZ.")
    def listefonk(list1):
        list1=[9,9,9]
        list1[2]=3
        print(list1)

    listefonk(list1)
    print(list1,"\n")

def dal13():
    '''13-CONCATENATION DETAY(+ ILE BIRLESTIRME)'''
    print("13- ASSIGNMENT VAR ISE IMMUTABLE DA OLSA VARIABLE YENIDEN OLUSTURULACAGINDAN\n"
      "ERROR ALINMAZ.")
    ad="ali"
    ad2=" veli"
    ad=ad+ad2
    print(ad)




dict1={}
dict1['ali']=9
print(dict1)


