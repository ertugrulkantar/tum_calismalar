
package deneme;


public class Deneme {

   
    public static void main(String[] args) {
        
        Student ogrenci1=new Student("İbrahim","Kaya","509876",3);
        Student ogrenci2=new Student("Aysel","Polat","589123",4);
        System.out.println(ogrenci1);
        System.out.println(ogrenci2);
        Student ogrenci3=new Student(ogrenci2);
        
        if (ogrenci3.equals(ogrenci2))
            System.out.println("Nesneler esit.");
        else
            System.out.println("Nesneler esit degil.");
                
    
    
    }
    
    
}
