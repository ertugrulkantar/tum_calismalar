
package pkg5.lab_4_uygulamalar;

public class Daire {
    private double yariCap;
    private Nokta merkez;
    
    public Daire(double ycap,Nokta n){
        yariCap=ycap;
        merkez=n;}
    
    public String toString(){
        return "Yaricap:"+getYariCap()+" merkez:"+getMerkez().toString();
    }

    /**
     * @return the yariCap
     */
    public double getYariCap() {
        return yariCap;
    }

    /**
     * @param yariCap the yariCap to set
     */
    public void setYariCap(double yariCap) {
        this.yariCap = yariCap;
    }

    /**
     * @return the merkez
     */
    public Nokta getMerkez() {
        return merkez;
    }

    /**
     * @param merkez the merkez to set
     */
    public void setMerkez(Nokta merkez) {
        this.merkez = merkez;
    }
    public double alanHesapla(){
        return getYariCap()*getYariCap()*3.14;
    }
    public double cevreHesapla(){
        return getYariCap()*2*3.14;
    }
    
    public boolean equals(Daire otherDaire){
        return ((merkez.equals(otherDaire.getMerkez()))&&yariCap==otherDaire.getYariCap());
        
        
    }
    
}
