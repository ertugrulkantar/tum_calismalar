
package pkgfinal;


public class Car extends Vehicle {
   //extends Vehicle::Car class'ının Vehicle sınıfının subclasss'ı olduğu anlamına geliyor.
    
   private int kapiSayisi; //Car class'ı için istenilen değişken.
   
   public Car(String plaka,String model,String marka,int kapiSayisi)
   /*Tüm değişkenleri içeren constructor metot.*/
   {
       super(plaka,model,marka); //Superclass'ın constructor'unu çağırıyoruz ve gerekli argümanları veriyoruz.
       this.kapiSayisi=kapiSayisi; //Car'a ait kapiSayisi değişkenini atıyoruz.
   }
   
    //Gerekli GET-SET metotları başlangıcı.
    public int getKapiSayisi() {
        return kapiSayisi;
    }

    public void setKapiSayisi(int kapiSayisi) {
        this.kapiSayisi = kapiSayisi;
    }
    //GET-SET metotları sonu.
    
    public String toString()
    /*Sınıfa ait nesneleri yazdırmak için gereken toString metodu.*/
    {
        String pre=super.toString(); //super'in toString'ini bu class'ta kullanarak işlemi kolaylaştırıyoruz.
        return(pre+"\nKapi Sayisi::"+getKapiSayisi());
    }
   
   
   
}
