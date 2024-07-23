/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package deneme;

/**
 *
 * @author ahmet
 */
public class Person {
    private String ad;
    private String soyad;

 
    public String getAd() {
        return ad;
    }

    
    public void setAd(String ad) {
        this.ad = ad;
    }

   
    public String getSoyad() {
        return soyad;
    }

 
    public void setSoyad(String soyad) {
        this.soyad = soyad;
    }
 
    public Person()     //Parametresiz constructor.
    {
        ad="Ad yok!";
        soyad="Soyad yok!";
    }
    
    public Person(String ad,String soyad)   //Tüm değişkenlere sahip constructor.
    {
        if(ad==null || soyad==null)
        {
            System.out.println("Person olusturmada hata!");
            System.exit(0);
        }
        
        this.ad=ad;
        this.soyad=soyad;
    }
    
    public Person(Person orjinalPerson)     //Copy constructor.
    {
        ad=orjinalPerson.getAd();
        soyad=orjinalPerson.getSoyad();
    }
    
    public String toString()
    {
        return("Ad::"+getAd()+" Soyad::"+getSoyad());
    }
    
    
}
