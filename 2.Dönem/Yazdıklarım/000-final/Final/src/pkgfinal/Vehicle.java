
package pkgfinal;


public class Vehicle implements Comparable { 
    /*implements Comparable::Vehicle sınıfı Comparable'yi gerçekleştirir anlamına geliyor.*/
    
    private String plaka; //Vehicle class'ı için 
    private String model; //istenilen değişkenler
    private String marka; //private olarak oluşturuldu.  
    
    public Vehicle(String plaka,String model,String marka) 
    /*Tüm değişkenleri içeren constructor metot.*/
    {
        this.plaka=plaka;   //Burada parametreler sınıfın değişkenlerine atanıyor.
        this.model=model;   //this.*** ise ***'ın sınıf değişkenini işaret ettiğini belirtiyor.
        this.marka=marka;   //Böylece parametrelerle değişkenler karışmıyor.
    }
    
    //Gerekli GET-SET metotları başlangıcı.
    public String getPlaka() {
        return plaka;
    }

    public void setPlaka(String plaka) {
        this.plaka = plaka;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getMarka() {
        return marka;
    }

    public void setMarka(String marka) {
        this.marka = marka;
    }
    //GET-SET metotları sonu.
    
    
    public String toString()
    /*Sınıfa ait nesneleri yazdırmak için gereken toString metodu.*/        
    {
        return("Marka::"+getMarka()+" Model::"+getModel()+" Plaka::"+getPlaka());
    }
    
    public int compareTo(Object other)
    /*compareTo metodunun gerçekleştirimi.Metot plaka karşılaştırmasına göre -1,0,1 döndürecek.*/
    {
        Vehicle otherVehicle=(Vehicle) other; //Karşılaştırılacak diğer nesne Vehicle sınıfında tanımlanıyor.
        return getPlaka().compareTo(otherVehicle.getPlaka());  
    
    /*Metot 2 nesne aynıysa 0, karşılaştırmadaki ilk nesne alfabede daha sonraysa pozitif
        bir sayı,karşılaştırmadaki ikinci nesne alfabede daha sonraysa negatif bir sayı 
        döndürür.*/
    
    }

    
    
}
