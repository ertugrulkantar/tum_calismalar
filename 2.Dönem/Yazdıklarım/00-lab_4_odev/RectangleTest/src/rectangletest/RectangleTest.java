
package rectangletest;


public class RectangleTest {

    
    public static void main(String[] args) {
        Rectangle dikdortgen1=new Rectangle(5,6);
        Rectangle dikdortgen2=new Rectangle(3,4);
        int alan=dikdortgen1.alanHesapla();//Bunu ödevde istendiği için yazdım ancak
        System.out.println(dikdortgen1);   //toString zaten alanı yazdırıyor o yüzden
                                           //işlevsiz kaldı.
        System.out.println("Su andaki nesne sayisi:"+Rectangle.getMevcut());    
    }                                           
    
}
