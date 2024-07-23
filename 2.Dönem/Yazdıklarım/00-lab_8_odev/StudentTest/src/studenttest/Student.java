
package studenttest;


public class Student {
    
    private String ad;
    private String soyad;
    private String TCkimlikNo;
    private String adres;

    public Student()
    {
        ad=null;
        soyad=null;
        TCkimlikNo=null;
        adres=null;
    }
    
    
    public Student(String ad,String soyad,String TC,String adres)
    {
        if (ad==null || soyad==null || TC==null || adres==null)
        {
            System.out.println("Nesne olusturmada hata!!!");
            System.exit(0);        
        }
        this.ad=ad;
        this.soyad=soyad;
        TCkimlikNo=TC;
        this.adres=adres;
    }
    /**
     * @return the ad
     */
    public String getAd() {
        return ad;
    }

    /**
     * @param ad the ad to set
     */
    public void setAd(String ad) {
        this.ad = ad;
    }

    /**
     * @return the soyad
     */
    public String getSoyad() {
        return soyad;
    }

    /**
     * @param soyad the soyad to set
     */
    public void setSoyad(String soyad) {
        this.soyad = soyad;
    }

    /**
     * @return the TCkimlikNo
     */
    public String getTCkimlikNo() {
        return TCkimlikNo;
    }

    /**
     * @param TCkimlikNo the TCkimlikNo to set
     */
    public void setTCkimlikNo(String TCkimlikNo) {
        this.TCkimlikNo = TCkimlikNo;
    }

    /**
     * @return the adres
     */
    public String getAdres() {
        return adres;
    }

    /**
     * @param adres the adres to set
     */
    public void setAdres(String adres) {
        this.adres = adres;
    }
    
    public String toString()
    {
        return ("Ad::"+getAd()+" Soyad::"+getSoyad()+"\nT.C. Kimlik::"+getTCkimlikNo()+" Adres::"+getAdres());
    }
}
