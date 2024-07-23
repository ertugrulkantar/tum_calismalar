#cursor: bu yanıp sönen işaret
#f8 f9 step in step out falan var.
#debug'u evde öğren.

import random
sayi=random.randint(1,100)
tahmin=int(input('Sayiyi tahmin et(1-100)'))

tahmin_say=1

while sayi!=tahmin:
    if tahmin<sayi:
        print('Yukari')
    else:
        print('Asagi')
    tahmin=int(input('Yeni tahmininiz'))
    tahmin_say+=1

print('Tebrikler!',tahmin,'sayisini dogru tahmin ettiniz.')
print('Tahmin denemeniz:',tahmin_say)

end=input()