#haftanın kaçıncı günü olduğu girildiğinde
#o günün adını ve mesai/tatil günü olduğunu
#belirleyen program.
#elif alıştırması.

kacinci_gun=int(input('haftanin kacinci gunundeyiz::'))

if kacinci_gun==1:
    print('Pazartesi',end='-')
elif kacinci_gun==2:
    print('Sali',end='-')
elif kacinci_gun==3:
    print('Carsamba',end='-')
elif kacinci_gun==4:
    print('Persembe',end='-')
elif kacinci_gun==5:
    print('Cuma',end='-')
elif kacinci_gun==6:
    print('Cumartesi',end='-')
elif kacinci_gun==7:
    print('Pazar',end='-')
else:
    print('Hatali giris')

if kacinci_gun==1 or kacinci_gun==2 or kacinci_gun==3 or kacinci_gun==4 or kacinci_gun==5:
    print('Hafta ici')
elif kacinci_gun==6 or kacinci_gun==7:
    print('Hafta sonu')

end=input()