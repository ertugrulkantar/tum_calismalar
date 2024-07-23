#0 ile 100 arasındaki çift sayıların toplamını hesaplar.
#1.versiyon 'while' ile

n=100
toplam=0 #döngüler için toplama değeri.

while n!=0:
    toplam+=n
    n-=2
print('Toplam(while ile)',toplam,sep='=')

#2.versiyon 'for' ile

n2=100
toplam2=0 #döngüler için toplama değeri.

for sayac in range(n2,0,-2):
    toplam2+=sayac

print('Toplam(for ile)',toplam2,sep='=')

end=input()


