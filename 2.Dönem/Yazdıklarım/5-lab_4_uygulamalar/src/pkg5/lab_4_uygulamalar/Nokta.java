//Encapsulation??
package pkg5.lab_4_uygulamalar;

public class Nokta {
    private int X,Y;
    
    public Nokta(int x,int y){
        X=x;
        Y=y;}
    
    @Override
    public String toString(){
        return "X="+getX()+" Y="+getY();
    }

    /**
     * @return the X
     */
    public int getX() {
        return X;
    }

    /**
     * @param X the X to set
     */
    public void setX(int X) {
        this.X = X;
    }

    /**
     * @return the Y
     */
    public int getY() {
        return Y;
    }

    /**
     * @param Y the Y to set
     */
    public void setY(int Y) {
        this.Y = Y;
    }
    
    public boolean equals(Nokta otherNokta){
        return ((X==otherNokta.getX())&&Y==otherNokta.getY());
        
    }
}
