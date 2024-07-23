
package polymorphism;


public class Dog extends EvcilHayvan {
    
    private String cins;
    
    public Dog(String hayvanIsmi,int hayvanYasi,double agirlik,String cins)
    {
        super(hayvanIsmi, hayvanYasi, agirlik);
        this.cins=cins;
    }

 
    public String getCins()
    {
        return cins;
    }

   
    public void setCins(String cins) 
    {
        this.cins=cins;
    }
    
    
    public String toString()
    {
        String sonuc=super.toString();
        return sonuc+"Cinsi::" + getCins();
    }

    public void ilac01Dozaj()
    {
        System.out.println("ilac01Dozaj::"+(getAgirlik()/2.2) * (0.03/10));
    }

    public void ilac02Dozaj()
    {
        System.out.println("ilac02Dozaj::"+(getAgirlik()/2.2)*(0.5/12));
    }
    
    
    
    
}
