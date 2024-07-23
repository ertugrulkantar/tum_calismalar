#Faktöriyel hesaplar.

#1.versiyon:'while' ile

n=int(input('Kacinci faktoriyeli istersiniz::'))
carpim=1      #çarpım döngüleri için başlangıç değeri.
carpan=n

while carpan>1:
    carpim*=carpan
    carpan-=1
print(n,'.faktoriyel=',carpim,sep='')

end=input()

