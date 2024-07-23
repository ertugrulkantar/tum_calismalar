
package polymorphism;


public class Cat extends EvcilHayvan {
    private String renk;
    
    public Cat(String hayvanIsmi, int hayvanYasi, double agirlik, String renk)
    {
        super(hayvanIsmi,hayvanYasi,agirlik);
        this.renk=renk;
    }


    public String getRenk()
    {
        return renk;
    }

  
    public void setRenk(String renk) 
    {
        this.renk=renk;
    }
    
    public String toString()
    {
        String sonuc2=super.toString();
        return sonuc2+"Rengi::"+getRenk();
    }

    public void ilac01Dozaj()
    {
        System.out.println("ilac01Dozaj::"+(getAgirlik()/2.2)*(0.002/10));
    }

    public void ilac02Dozaj()
    {
        System.out.println("ilac02Dozaj::"+(getAgirlik()/2.2)*(0.25/12));
    }
    
    
    
}
