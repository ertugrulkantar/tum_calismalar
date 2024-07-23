
package pkgfinal;


public class Truck extends Vehicle {
    //extends Vehicle::Truck class'ının Vehicle sınıfının subclasss'ı olduğu anlamına geliyor.
    
    private int yukKapasitesi; //Truck class'ı için istenilen değişken.
   
    public Truck(String plaka,String model,String marka,int yukKapasitesi)
    {
        super(plaka,model,marka); //Superclass'ın constructor'unu çağırıyoruz ve gerekli argümanları veriyoruz.
        this.yukKapasitesi=yukKapasitesi;   //Truck'a ait yukKapasitesi değişkenini atıyoruz.
    }
    
    //Gerekli GET-SET metotları başlangıcı.
    public int getYukKapasitesi() {
        return yukKapasitesi;
    }

    public void setYukKapasitesi(int yukKapasitesi) {
        this.yukKapasitesi = yukKapasitesi;
    }
    //GET-SET metotları sonu.
    
    public String toString()
    /*Sınıfa ait nesneleri yazdırmak için gereken toString metodu.*/
    {
        String pre=super.toString(); //super'in toString'ini bu class'ta kullanarak işlemi kolaylaştırıyoruz.
        return(pre+"\nYuk Kapasitesi::"+getYukKapasitesi());
    }
}
