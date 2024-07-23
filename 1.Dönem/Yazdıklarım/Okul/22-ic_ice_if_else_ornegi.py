#Girilen notu harflendirir.
#iç içe if-else örneği.
#vize ortalaması 75 üstü ise finalsiz geçme var.

VIZE_AGIRLIGI=0.6
FINAL_AGIRLIGI=0.4


vize1=int(input('vize1::'))
vize2=int(input('vize2::'))
vize_ortalamasi=(vize1+vize2)/2

if vize_ortalamasi>=75:
    print('Finalden Muafsın')
else:
    final=int(input('final::'))
    if vize_ortalamasi*VIZE_AGIRLIGI+final*FINAL_AGIRLIGI>=60:
        print('Gectin')
    else:
        print('Kaldin')

end=input()