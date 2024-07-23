
package sort;


public class InsertionSort {
    public static void sirala(int dizi[])
    {
        int dizi_uzunlugu=dizi.length;  //Dizi uzunluğunu değişkene atadım.
        for (int i=1;i<dizi_uzunlugu;i++)   //Diziyi dolaşmak için for loop kullandım.
        {
            int siradaki_sayi=dizi[i];   //Bunu elde tutup diziyi kaydırdırtan sonra oluşan boşluğa yerleştireceğiz.
            int k=i-1;  //Bir önceki index ile karşılaştırmaya başlayacağız.
            while (k>=0 && dizi[k]>siradaki_sayi)
            {
                dizi[k+1]=dizi[k];  //Eğer koşul sağlanıyorsa kaydırıyoruz.
                k-=1;           //Ve k'yi azaltarak bir önceki index ile elimizdekini karşılaştırıyoruz.
            }
            dizi[k+1]=siradaki_sayi;    //Oluşan uygun boşluğa sayıyı sıkıştırıyoruz.
        }                               //Böylece elimizde her döngüde sıralı alt diziler oluyor.
    }                                   //Döngü tamamen bittiğinde tüm dizi sıralı hale geliyor.
}
        
    
    
    
        

