#bu program askeriyeye kabulünüzü sınar.

boy=int(input('boyunuzu giriniz::'))
kilo=int(input('kilonuzu giriniz::'))
BOY_SİNİRİ=175
KİLO_SİNİRİ=75

if boy>=BOY_SİNİRİ and kilo<=KİLO_SİNİRİ:
    print('Askersin!')
else:
    print('Maalesef :(')

#2.yol
print('2.yol::')

boy2=int(input('boyunuzu giriniz::'))
kilo2=int(input('kilonuzu giriniz::'))

if not(boy2>=BOY_SİNİRİ and kilo2<=KİLO_SİNİRİ):
    print('Maalesef :(')
else:
    print('Askersin!')

end=input()