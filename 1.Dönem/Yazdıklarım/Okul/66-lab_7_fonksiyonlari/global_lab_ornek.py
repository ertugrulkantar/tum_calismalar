a=5
            #Scope:Etki alanı.
def can():
    #global a       #Eğer baştaki #'yi silersen global çalışır; a 7 olur.
    a=7
    return a    #Bu 'a'yı değil;'can' fonksiyonuna atanır.

can()
print(can())
print(a)