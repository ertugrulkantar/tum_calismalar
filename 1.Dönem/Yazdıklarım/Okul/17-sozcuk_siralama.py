#bu program girilen sözcükleri alfabetik olarak sıralar.
#yani sözlükteki sıralama gibi düşünülebilir.

sozcuk1=input('1.sozcuk::')
sozcuk2=input('2.sozcuk:')

if sozcuk1>sozcuk2:
    print('ilk',sozcuk2,'ikinci',sozcuk1)
if sozcuk2>sozcuk1:
    print('ilk',sozcuk1,'ikinci',sozcuk2)

if sozcuk2==sozcuk1:
    print('sozcukler ayni.')

end=input()
