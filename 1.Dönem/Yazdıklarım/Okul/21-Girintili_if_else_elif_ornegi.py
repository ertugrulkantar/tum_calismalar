#Girintili if-else örneği
#Asker misin?

cinsiyet=input('cinsiyetiniz(e/k/E/K)::')
boy=int(input('boyunuz::'))
kilo=int(input('kilonuz::'))

if cinsiyet=='e' or cinsiyet=='E':
    if boy>175 and kilo<75:
        print('Askersin')
elif cinsiyet=='k' or cinsiyet=='K':
    if boy>165 and kilo<65:
        print('Askersin')
    else:
        print('Malesef')
else:
    print('Hatali Giris')

end=input()
