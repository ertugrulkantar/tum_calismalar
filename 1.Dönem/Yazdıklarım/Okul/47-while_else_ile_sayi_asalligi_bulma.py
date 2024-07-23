import math
sayi=int(input('Sayiyi giriniz::'))


while sayi>1:
    for bolen in range(2,int(math.sqrt(sayi)+1)):
        if sayi%bolen==0:
            print('Asal degil')
            break
    else:
        print('Asal')

    sayi=int(input('Yeni sayi::'))

end=input()