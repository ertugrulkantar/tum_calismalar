
package pkg6.lab_3_odev;

import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class Lab_3_odev {

    public static void main(String[] args) {
        Scanner fileText=null;
        
        try{
            fileText=new Scanner(new FileInputStream("words.txt"));}
        
        catch (FileNotFoundException e){
            System.out.println("Dosya bulunamadi!!!");
            System.exit(0);}
        
        String kelime;
        int siraliUnluSay;
        int maximumSiralisiraliUnluSay=0;
        String maximumSiraliUnluluKelime="";
        System.out.println("4 tane sirali unlu iceren kelimeler\n------------------------------");
        
        while (fileText.hasNext()){
            kelime=fileText.next();
            siraliUnluSay=0;
            boolean yazildiMi=false;  /*--->Arka arkaya 4 ünlüye sahip kelimelerin bir daha arka arkaya
                                       4 ünlüye sahipse yazdırılmasını önlemek amacıyla sentinel oluşturuldu*/
            int kelimeUzunlugu=kelime.length();
            
            for (int i=0; i<kelimeUzunlugu;i++){
                char harf=kelime.charAt(i);
                
                if (harf=='a' || harf=='e' || harf=='i' || harf=='o' || harf=='u'){
                    siraliUnluSay++;
                    if (siraliUnluSay==4 && kelimeUzunlugu==(i+1) && yazildiMi==false){ //else'e giremeyecek kelimeleri
                        System.out.println(kelime);                                     //yakalamak için.
                        yazildiMi=true;}
                    if (siraliUnluSay>=maximumSiralisiraliUnluSay){ //else'e giremeyecek kelimeleri
                        maximumSiralisiraliUnluSay=siraliUnluSay;   //yakalamak için.
                        maximumSiraliUnluluKelime=kelime;}}   
                else{
                    if (siraliUnluSay==4 && yazildiMi==false){
                        System.out.println(kelime);
                        yazildiMi=true;}
                    if (siraliUnluSay>=maximumSiralisiraliUnluSay){
                        maximumSiralisiraliUnluSay=siraliUnluSay;
                        maximumSiraliUnluluKelime=kelime;}
                    siraliUnluSay=0;}}}
        
        System.out.println("\nEn cok sirali unlu iceren kelime\n--------------------------------");
        System.out.println(maximumSiraliUnluluKelime);
    }}
            
       
            
            
       
    
    

