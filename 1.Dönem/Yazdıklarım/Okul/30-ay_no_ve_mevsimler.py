#30 gun ceken aylar daha az olduğu için ilk elif'te onları
#sorgulasan daha iyi olur.

ay_no=int(input('Kacinci aydayiz::'))
if ay_no>12 or ay_no<1:
    print('hatali giris')

elif ay_no==1 or ay_no==3 or ay_no==5 or ay_no==7 or ay_no==8 or ay_no==10 or ay_no==12:
    print('31 gun',end='-')
elif ay_no==2:
    print('28 gun',end='-')
else:
    print('30 gun',end='-')

if ay_no==12 or ay_no==1 or ay_no==2:
    print('kış')
elif ay_no==3 or ay_no==4 or ay_no==5:
    print('ilk bahar')
elif ay_no==6 or ay_no==7 or ay_no==8:
    print('yaz')
elif ay_no==9 or ay_no==10 or ay_no==11:
    print('sonbahar')
else:
    print('hatali giris')

end=input()

#hocanin yeni yontemi

ay_no_0_11=ay_no%12

if ay_no_0_11<3:
    print('KIŞ')
elif ay_no_0_11<6:
    print('İLKBAHAR')
elif ay_no_0_11<9:
    print('Yaz')
else:
    print('sonbahar')

end=input('')