yillik_toplam=0
max_aylik_toplam=0

for ay in range(12):
    aylik_toplam=0
    for gun in range(30):
        print(ay+1,'.ayin ',gun+1,'.gununun satisini giriniz::',sep='',end='')
        satis_miktari=int(input(''))
        aylik_toplam+=satis_miktari
    print(ay+1,'. ayin satis toplami=',aylik_toplam,sep='')
    yillik_toplam+=aylik_toplam
    if aylik_toplam>=max_aylik_toplam:
        max_aylik_toplam=aylik_toplam
        max_ay_no=ay+1

print('Yillik toplam=',yillik_toplam,sep='')
print('Aylik toplam=',aylik_toplam,sep='')
print('En fazla satis yapilan ay ',max_ay_no,' Satis miktari=',max_aylik_toplam,sep='')

end=input

