X_MIN=-3
X_MAX=3
Y_MIN=0
Y_MAX=3
f_toplam=0
gecersiz_sayi=0

for x in range(X_MIN,X_MAX+1):
    for y in range(Y_MIN,Y_MAX+1):
        if x+y!=0:
            f=(2*x+3*y-4*x*y+5)/(x+y)
            print('f(',x,',',y,')=',round(f,2),sep='')
            f_toplam+=f
        else:
            print('f(',x,',',y,')=','icin sonuc yok')
            gecersiz_sayi+=1

print('Sonuclarin ortalamasi:',f_toplam/(X_MAX-X_MIN+1))

end=input()