print('bu_program_yasadiginiz_toplam_dk_yi_hesaplar')
yil = int(input('dogum_yiliniz'))
ay = int(input('dogdugunuz_ayin_sayısal_karsiligi'))
gun = int(input('dogdugunuz_ayin_kacinci_gunu_dogdununuz'))
x = int((31 - gun) * 1440)  #gun_icin_hesaplama
y = int(9 - ay)
z = int(2019 - yil)  #ay_ve_yil_icin_hesaplama
       
if y >= 0:
    y = int(y * 43200)
    z = int(z * 518400)
else:
    y = int((12 + y) * 43200)
    z = int((z - 1) * 518400)
toplam_dk = int(x + y + z)
if toplam_dk<=0 :
    print('gelecekten_hosgeldin_yabanci')
if toplam_dk>0:
     print('su_ana_kadar_toplam', toplam_dk, 'dk_kadar_yasadiniz') ;\


         
print('bu_program_Muharrem_abim_icin_yazildi')
print('ins_begenirsin_abi_ilk_programim')
print('kendine_iyi_bak')
gg=input('end')
