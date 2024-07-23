#2.versiyon:'for' ile faktöriyel hesaplama.

n=int(input('Kacinci faktoriyeli istersiniz:'))

carpim=1 #döngü için çarpim değeri.

for carpan in range(n,1,-1):
    carpim*=carpan


print(n,'.farktoriyel=',carpim,sep='')

end=input()