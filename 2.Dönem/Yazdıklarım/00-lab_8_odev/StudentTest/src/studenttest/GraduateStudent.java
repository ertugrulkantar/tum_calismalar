
package studenttest;



public class GraduateStudent extends Student {
    private String tezBasligi;

    /**
     * @return the tezBasligi
     */
    public String getTezBasligi() {
        return tezBasligi;
    }

    /**
     * @param tezBasligi the tezBasligi to set
     */
    public void setTezBasligi(String tezBasligi) {
        this.tezBasligi = tezBasligi;
    }
    
    public GraduateStudent(String ad,String soyad,String TC,String adres,String tezbasligi)
    {
        super(ad,soyad,TC,adres);
        if (tezbasligi==null)
        {
            System.out.println("Nesne olusturmada hata!!!");
            System.exit(0);
        }
        tezBasligi=tezbasligi;
    }
    
    public String toString()
    {
        String pre=super.toString();
        return(pre+"\nTez Basligi::"+getTezBasligi());
    }
           
}
