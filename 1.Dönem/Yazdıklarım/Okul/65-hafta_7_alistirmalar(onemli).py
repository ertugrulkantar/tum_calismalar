import random
import math

def deneme():
    x=5
    y=4
    print(y)
    z=6
    k=7
    return x,y,z,k  #direkt bunları printleyemiyorsun.
                    #neden bilmiyorum.Galiba return x,y,z,k ya değil de direkt deneme fonksiyonuna
                    #değer atıyor.
print(deneme())
#print(k)  bu niye printlenemiyo başındaki '#'silinse de?
a,b,c,d=deneme()

print(a,b)
print(c)  #returnda z'yi silersen error verir.


def message():
    print('I am sıpıdık')
    print('King of nothing')

def main():
    print('I am main.')
    print('King of program')
    message()
    print('You have seen the message of the message function')
    print('GG')


print(random.randrange(0,101,10))  #randrange 0-100 rastgele sayı 10'ar adımla.
print((random.random())) #0.00-1.00 arası float üretir.(1 dahil değil)
print(random.uniform(1,10)) #random.random'un aralık içeren hali.

#random.seed(5)  #seed'i (normalde system clock) sabitler.

def sum(num1,num2):
    '''İki sayıyı toplar.'''
    return num1+num2    #num1+num2'yi değişkene atamak yerine direkt return'la döndürebilirsin.
print(sum(5,3))

def main():
    brut_tutar=int(input('Brut tutari giriniz::'))
    net_tutar=brut_tutar-indirim(brut_tutar)
    return net_tutar

def indirim(brut_tutar):
    INDIRIM_YUZDESI=int(input('Indırım yuzdesini giriniz::'))
    return brut_tutar*INDIRIM_YUZDESI

print(main())  #Sonuçta indirim fonksiyonu çağırılmadan önce tanımlandı.So nop.

def hipotenus(kenar1,kenar2):
    '''İki kenarı girilen dik üçgenin hipotenüsünü hesaplar'''
    c=math.hypot(kenar1,kenar2)
    print(kenar1,kenar2,'nin hipotenusu::',c)

hipotenus(5,12)

def length(a_str):
    """Return the length of a str"""
    count = 0
    for char in a_str:     #her harf for'u 1 kez döndürür.
        count += 1
    return count
print('hiyar sozcugu uzunlugu::',length('HIYAR'))

