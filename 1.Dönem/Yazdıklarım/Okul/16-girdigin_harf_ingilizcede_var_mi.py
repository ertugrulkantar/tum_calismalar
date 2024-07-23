#bu program girilen bir karakterin(harfin) İngilizce'de olan bir karakter olup olmadığını
#kontrol eder.

harf=input('harfi giriniz**buyuk kucuk fark etmez**:')

if 'A'<=harf<='Z' or   'a'<=harf<='z':
    print('''harf İngilizce'de mevcut''')
else:
    print('''harf İngilizce'de mevcut degil''')

end=input()