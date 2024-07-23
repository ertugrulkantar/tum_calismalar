package deneme;


public class Customer {
    
    private String adSoyad;
    private String adres;
    
    public Customer(String musteriAdiSoyadi,String musteriAdresi)
    {
        adSoyad=musteriAdiSoyadi;
        adres=musteriAdresi;
    }
    
    public String toString()
    {
        return(adSoyad+", "+adres);
    }
            
}
