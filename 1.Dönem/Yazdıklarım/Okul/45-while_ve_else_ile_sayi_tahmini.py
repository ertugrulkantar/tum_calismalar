import random  # random kütüphanesi, rasgele sayı üretimi ile ilgili hazır fonksiyonları içerir.

min_tahmin_say = 100
tekrar='e'
while tekrar=='e' or tekrar=='E':  # En az 1 kez girmesi isteniyor ama Python'da koşul sona yazılamadığı için sonsuz döngü yapıldı.
    sayi = random.randint(1, 100)  # randint(min,max) fonksiyonu, min ile max arasında rasgele bir tamsayı döndürür.
    tahmin_say = 0
    tahmin = int(input("Lütfen tahmini bir sayı giriniz:"))
    tahmin_say += 1

    while sayi != tahmin:
        if tahmin < sayi:
            print("YUKARI!")
        else:
            print("AŞAĞI!")

        tahmin = int(input("Lütfen tahmini bir sayı giriniz:"))
        tahmin_say += 1

    print("TEBRİKLER! Doğru tahmin ettiniz.")
    print(tahmin_say, "tahminde bilgisayarın tuttuğu sayıyı buldunuz.")
    if tahmin_say < min_tahmin_say:
        min_tahmin_say = tahmin_say

    tekrar = input("Tekrar oynamak ister misiniz(e/E/h/H)?")
    while tekrar not in ['e', 'E', 'h', 'H']:  # in operatörü, liste içerisinde belirli bir elemanın aranmasını sağlar.
        tekrar = input("Tekrar oynamak ister misiniz(e/E/h/H)?")

       #buradaki breaki silmesek ne olurdu???-evde bak.!!ne olur break tüm döngüyü kırar.

else:
    print("Hoşçakal")

end=input()






print("Tahmin sayısı rekoru:", min_tahmin_say)