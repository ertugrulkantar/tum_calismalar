/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package studenttest;

/**
 *
 * @author ahmet
 */
public class UnderGraduateStudent extends Student {
    
    private String ogrenciDanismani;

    
    public String getOgrenciDanismani() {
        return ogrenciDanismani;
    }

    
    public void setOgrenciDanismani(String ogrenciDanismani) {
        this.ogrenciDanismani = ogrenciDanismani;
    }
    
    public UnderGraduateStudent(String ad,String soyad,String TC,String adres,String danisman)
    {
        super(ad,soyad,TC,adres);
        if (danisman==null)
        {
            System.out.println("Ogrenci olusturmada hata!!!");
           System.exit(0);
        }
        ogrenciDanismani=danisman; 
    }
    
    public String toString()
    {
        String pre=super.toString();
        return(pre+"\nDanisman::"+getOgrenciDanismani());
    }
           
    
}
