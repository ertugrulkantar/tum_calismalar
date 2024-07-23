#Satır sayısı girildiğinde satır sayısı kadar uzunlukta
#ikizkenar üçgen oluşturur.7.hafta örneği.

satir_say=int(input('Satir sayisini giriniz::')) #3

for satir_no in range(1,satir_say+1):
    for i in range(satir_say-satir_no):
        print(' ',end='')
    for j in range(2*satir_no-1):
        print('*',end='')
    print('\n')

end=input()
