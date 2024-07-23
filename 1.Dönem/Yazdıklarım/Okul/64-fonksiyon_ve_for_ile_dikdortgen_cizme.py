def dikdortgen_ciz(dikey_kenar,yatay_kenar):
    dikey_kenar=int(input('Dik kenar uzunluğunu giriniz::'))
    yatay_kenar=int(input('Yatay kenar uzunluğunu giriniz::'))
    for j in range(dikey_kenar):
        for i in range(yatay_kenar):
            print('*',end='')
        print('\n')

dikdortgen_ciz(3,5)
