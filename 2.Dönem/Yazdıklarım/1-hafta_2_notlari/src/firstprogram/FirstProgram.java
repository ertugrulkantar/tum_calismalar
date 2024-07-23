/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package firstprogram;
import java.util.Scanner;


/**
 *
 * @author ahmet
 */
public class FirstProgram {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        /*ilk örnek*-------------------------*/
        System.out.println("Hello reader.");
        System.out.println("Welcome to Java");
        
        System.out.println("Let's demonstrate a calculation.");
        int answer=2+2;
        System.out.println("2 plus 2 is "+answer);
        /*-------------------------------------*/
        
        /*Bir satırda birden çok declaration yapılabilir.*/
        int initialCount=50, finalCount=20;
        System.out.println(finalCount);
        
        int i=(int)5.5; //Solda declaration yapacaksan parantez kullan.
        System.out.println(i);
        
        /*increment ve decrement operatorleri*/
        int n=1;
        n=(++n);
        System.out.println(n);
        //++n ve n++ farkı
        int dene=2*(n++); //Çarp,daha sonra n'e 1 ekle.
        int dene2=2*(++n);  //Topla,sonra çarp.n'in değeri 1 artar.
        System.out.println("dene="+dene+" dene2="+dene2);
        System.out.println("n="+n);
        
        /*String metotları*/
        String greeting="Hello";
        int count=greeting.length(); //Karakterleri sayar.
        System.out.println("Karakter Sayısı="+count);
        
        System.out.println(greeting.equals("Hello")); //Aynı mı kontrol eder.
        System.out.println(greeting.equals("hello")); //CaseSensivity var.
        System.out.println(greeting.equalsIgnoreCase("hello")); //CaseSensivity kalktı.
        
        String meraba="Hi Mary";
        System.out.println(meraba.toLowerCase()); //Hepsini küçüğe çevirir.
        System.out.println(meraba.toUpperCase()); //Hepsini büyüğe çevirir.
        
        String bosluklu="     Merhaba       ";
        System.out.println(bosluklu.trim());    //Whitespaceleri yok eder.
        
        String harfkonum="Burası cokomelli.";
        System.out.println(harfkonum.charAt(3));    //İndexteki charı döndürür.
        System.out.println(harfkonum.substring(3,7));   //Slicing.End dahil değil.
        System.out.println(harfkonum.indexOf("i")); //Bulursa indexi,bulamazsa -1 döner.
        
        /*Sözlük sıralaması.Önceyse pozitif sayı,aynıysa '0', sonraysa negatif sayı döner.*/
        String anakarsilastirilacak="adventure";
        String karsilastirilacak1="adventure";
        String karsilastirilacak2="zoo";
        String karsilastirilacak3="above";
        System.out.println(anakarsilastirilacak.compareTo(karsilastirilacak1));
        System.out.println(anakarsilastirilacak.compareTo(karsilastirilacak2));
        System.out.println(anakarsilastirilacak.compareTo(karsilastirilacak3));
        
        /*printf metodu*/
        double price=19.8;
        System.out.print("$");
        System.out.printf("%6.2f",price);
        System.out.println(" each.");
        
        /*printf + ve - işlevi*/
        double value=12.123;
        System.out.printf("Starts%8.2fEnd",value);
        System.out.println();
        System.out.printf("Starts%-8.2fEnds",value);
        System.out.println();
        
        /*printf multiple arguments*/
        double price2=19.8;
        String name="magic apple";
        System.out.printf("$%6.2f for each %s.",price,name);
        System.out.println();
        System.out.println("Fantastic!!!");
        
        String adim="Ertugruuuul";
        System.out.printf("Adım %s.",adim);
        
        /*Input alma*/
        Scanner keyboard=new Scanner(System.in);
        int numberOfPods=keyboard.nextInt();
        double d1=keyboard.nextDouble();
        
        /*nextLine metodu whitespaceden whitespaceye alır.Yani arta kalanı alır
        gibi düşünebilirsin.*/
        String word1=keyboard.nextLine();
        String word2=keyboard.nextLine();
        System.out.println(word2);
        
        
        
        
        
        
        
        
        
        
                
    }
    
}
