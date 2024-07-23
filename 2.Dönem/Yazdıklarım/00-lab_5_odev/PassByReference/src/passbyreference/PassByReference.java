
package passbyreference;

public class PassByReference {

   
    public static void main(String[] args) {
        TarihiDegistir tarih1=new TarihiDegistir(3,"Temmuz",1900);
        TarihiDegistir tarih2=new TarihiDegistir(20,"Aralik",3000);
        System.out.println("Su anda gecerli tarihimiz::"+tarih2);
        System.out.println("Simdi bu tarihi metoda arguman olarak geciyoruz");
        tarih1.HadiDegistir(tarih2);
        System.out.println("Metottan ciktiktan sonra tarihimiz::"+tarih2);
        
    }
    
}
