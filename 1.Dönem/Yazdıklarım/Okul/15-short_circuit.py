#bu program dersten geçip geçmediğinizi belirler.

ARASINAV_ORANI=0.4
FINAL_ORANI=0.6

ara1=int(input('1.ara sinav:'))
ara2=int(input('2.ara sinav::'))
final1=int(input('finav::'))

donem_sonu=(ara1+ara2)/2*ARASINAV_ORANI+final*FINAL_ORANI

if final>=60 and donem_sonu>=60:
    print('gectin')
else:
    print('kaldin')

print('SHORT-CIRCUİT-VERSIONU')

#SHORT-CİRCUİT VERSİYONU

arasinav1=int(input('ara1::'))
arasinav2=int(input('ara2::'))
final2=int(input('final::'))

if final2>=60 and (arasinav1+arasinav2)/2*ARASINAV_ORANI+final2*FINAL_ORANI>=60:
    print('gectin')
else:
    print('kaldin')

end=input()