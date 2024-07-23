import dikdortgen
import kuvvet

alan,cevre,kare=dikdortgen.dikdortgen()
print('Dikdortgenin alani:',alan,'Dikdortgenin cevresi',cevre)
if kare==True:
    print('Bu dikdortgen bir kare!')
else:
    print('Bu dikdortgen bir kare degil!')

kenar1=int(input('Dikdortgenin bir kenarının uzunlugunu giriniz::'))
kenar2=int(input('Dikdortgenin diger kenarının uzunlugunu giriniz::'))

alan,cevre,kare=dikdortgen.dikdortgen(kenar1,kenar2)
print('Dikdortgenin alani:',alan,'Dikdortgenin cevresi',cevre)
if kare==True:
    print('Bu dikdortgen bir kare!')
else:
    print('Bu dikdortgen bir kare degil!')

taban=int(input('Tabani giriniz::'))
us=int(input('Ussu giriniz::'))
print(taban,'uzeri',us,'==',kuvvet.kuvvet(taban,us))
