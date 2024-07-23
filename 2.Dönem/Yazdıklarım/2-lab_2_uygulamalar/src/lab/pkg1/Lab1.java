/*
 *
 */
package lab.pkg1;
import java.util.Scanner;  //Scanner bir sınıf.

public class Lab1 {

 
    public static void main(String[] args) {
        Scanner klavye=new Scanner(System.in);  //klavye Scanner clasından yaratılan bir nesne.
        
        String ad;
        String soyad;
        
        System.out.println("Adinizi giriniz:");
        ad=klavye.nextLine();
        
        System.out.println("Soyadinizi giriniz:");
        soyad=klavye.nextLine();
        
        ad=ad.toLowerCase();  //ad ve soyadın tüm harflerini küçük harfe dönüştürdü.
        soyad=soyad.toLowerCase();
        
        System.out.println("Adinizi ve Soyadinizin Sifrelenmis Hali:");
        
        String sifreliAd=ad.substring(1,ad.length())+ad.substring(0,1)+"ay";  //2.argüman verilmezse ne olur?
        sifreliAd=sifreliAd.substring(0,1).toUpperCase()+sifreliAd.substring(1,sifreliAd.length());
        /*2.argüman verilmezse ilk indexten sona kadar gider.*/
        
        String sifreliSoyad=soyad.substring(1,soyad.length())+soyad.substring(0,1)+"ay";
        sifreliSoyad=sifreliSoyad.substring(0,1).toUpperCase()+sifreliSoyad.substring(1,sifreliSoyad.length());
        
        System.out.println(sifreliAd+" "+sifreliSoyad);
        
        
        
        
        
        
        
        
    }
    
}
