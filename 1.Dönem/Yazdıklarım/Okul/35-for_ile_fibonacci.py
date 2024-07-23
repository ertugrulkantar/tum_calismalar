#Fibonacci serisi heaplar.

n=int(input('Kacinci Fibonacci sayisini istersiniz::'))
iki_onceki=0
bir_onceki=1

if n==1 or n==0:
    print(n,'.fibonacci sayisi=',n,sep='')
else:
    for sayac in range(2,n+1):
        fibonacci=iki_onceki+bir_onceki
        iki_onceki=bir_onceki
        bir_onceki=fibonacci

if n!=1 and n!=0:
    print(n,'.fibonacci sayisi=',fibonacci,sep='')

end=input()