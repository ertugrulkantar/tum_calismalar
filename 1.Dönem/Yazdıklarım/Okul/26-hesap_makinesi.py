#hesap makinesi
#elif örneği

print('Bu bir hesap makinesidir.')

sayi1=float(input('birinci sayi::'))
sayi2=float(input('ikinci sayi::'))
islem_operatoru=input('islem operatorunu giriniz-secenekler:+,-,*,/')

if not(islem_operatoru=='+' or islem_operatoru=='-' or islem_operatoru=='*' or islem_operatoru=='/'):
    print('Hatali Giris')
elif islem_operatoru=='+':
    sonuc=sayi1+sayi2
    sonuc = round(sonuc, 2)
    print('Sonuc=', sonuc, sep='' )
elif islem_operatoru=='-':
    sonuc=sayi1-sayi2
    sonuc = round(sonuc, 2)
    print('Sonuc=', sonuc, sep='' )
elif islem_operatoru=='*':
    sonuc=sayi1*sayi2
    sonuc = round(sonuc, 2)
    print('Sonuc=', sonuc, sep='' )
else:
    if islem_operatoru=='/' and sayi2==0:
        print('Sifira bolme hatasi')
    elif islem_operatoru=='/':
        sonuc=sayi1/sayi2
        sonuc = round(sonuc, 2)
        print('Sonuc=', sonuc, sep='' )

end=input('end')