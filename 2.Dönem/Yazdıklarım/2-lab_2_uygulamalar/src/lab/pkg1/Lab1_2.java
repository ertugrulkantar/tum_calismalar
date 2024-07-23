
package lab.pkg1;

import java.util.Scanner;
import java.io.FileInputStream; //Dosyayı okumak için.
import java.io.FileNotFoundException;   //try-catch bloğu için.
import java.util.Formatter; //Çıktı formatlayabilmek için.

public class Lab1_2 {

    public static void main(String[] args) {
        
        Scanner fileIn=null;
        
                try{
                    fileIn=new Scanner(new FileInputStream("drink.txt"));
                    
                }catch(FileNotFoundException e){
                    
                    System.out.println("drink.txt not found");
                    System.exit(0); //Sistemi kapatır.
                }
        int mgCaffeinePerDrink=0;
        int mgFatal=10*1000;    //Ölümcül doz.
        
        String drinkName="";
        drinkName=fileIn.nextLine();
        
        mgCaffeinePerDrink=fileIn.nextInt();
        
        double drinkFatal=(double)mgFatal/mgCaffeinePerDrink;
        
        System.out.println("It will approximately "+drinkFatal+" drinks of "+drinkName+" at "+ mgCaffeinePerDrink
        +"mg of caffeine per drink to be lethal.");
        
        /*Formatlı yazdırma*/
        System.out.printf("It will approximately %4.2f drinks of %s at %s mg of "
                + "caffeine per drink to be lethal.",drinkFatal,drinkName,mgCaffeinePerDrink);
        
        /*Formatlı yazdırma 2.yol*/
        Formatter formatter=new Formatter();
        //formatter.format("")--->Burasını tamamlayamadım.
        
        fileIn.close();  //Dosya okuması bittikten sonra kapat.
        
        
        
        
        
  
    
    
    
    
    
    
    
    }
}