
package polymorphism;


public abstract class EvcilHayvan {
    private String hayvanIsmi;
    private int hayvanYasi;
    private double agirlik;
    
    public EvcilHayvan(String hayvanIsmi,int hayvanYasi,double agirlik)
    {
        this.hayvanIsmi=hayvanIsmi;
        setHayvanYasi(hayvanYasi);
        setAgirlik(agirlik);
    }
    

    
    public String getHayvanIsmi() 
    {
        return hayvanIsmi;
    }

  
    public void setHayvanIsmi(String hayvanIsmi)
    {
        this.hayvanIsmi=hayvanIsmi;
    }

 
    public int getHayvanYasi() 
    {
        return hayvanYasi;
    }

    
   
    public void setHayvanYasi(int hayvanYasi) 
    {
        if (hayvanYasi<0)
        {
            System.out.println("Hatali giris!!!");
            System.exit(0);
        }
        else
            this.hayvanYasi=hayvanYasi;
    }

    
    public double getAgirlik() 
    {
        return agirlik;
    }

  
    public void setAgirlik(double agirlik) 
    {
        if (agirlik<0){
            System.out.println("Hatali giris!!!");
            System.exit(0);
        }
        else
            this.agirlik=agirlik;
    }
    
    
    public String toString(){
        return "Hayvanın Adi::"+getHayvanIsmi()+" Hayvanin Yasi::"+getHayvanYasi()+" Hayvanin Agirligi::"+getAgirlik()+"Pound ";
    }
    
    public abstract void ilac01Dozaj();
    public abstract void ilac02Dozaj();
    
}
