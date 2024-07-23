#Collatz problemi
#Punch'n Enbody Chap2.4

sayi=int(input('Pozitif bir sayi giriniz::'))
sayac=0

while sayi>0:
    while sayi!=1:
        if sayi%2==0:
            sayi/=2
        elif sayi%2==1:
            sayi=3*sayi+1
        sayac+=1

    print('Son sayi::',sayi)
    print('Collatz ispati',sayac,'. denemede cozuldu.')
    sayi=int(input('Baska sayi denemek ister misiniz::'))

end=input