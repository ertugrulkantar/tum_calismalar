package passbyvalue;


public class PassByValue {
    
    public static void main(String[] args) {
        
        System.out.println("Deger olarak 345 secelim.");
        int degerim=345;
        System.out.println("Bu degeri arguman olarak HadiDegistir'e verelim.");
        System.out.println("HadiDegistir verdigimiz argumani 9999'a esitleyecek");
        HadiDegistir.degistir(degerim);
        System.out.println("Metottan ciktiktan sonra degerimize tekrar bakalim.");
        System.out.println("Degerimiz 9999 degil ilk atadigimiz sayi olan "+degerim);
        
    }
    
}
