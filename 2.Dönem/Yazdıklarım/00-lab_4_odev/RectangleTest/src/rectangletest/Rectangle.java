
package rectangletest;


public class Rectangle {
    
    private int en;
    private int boy;
    private static int mevcut=0;
    
    public static int getMevcut()
    {
      return mevcut;  
    }
    public Rectangle(int en,int boy)
    {
        this.en=en;
        this.boy=boy;
        mevcut++;
    }

    public int getEn()
    {
        return en;
    }

    public int getBoy()
    {
        return boy;
    }

    public void setEn(int en)
    {
        this.en=en;
    }
    
    public void setBoy(int boy)
    {
        this.boy=boy;
    }
    
    public int alanHesapla()
    {
        return getEn()*getBoy();
    }
    
    public String toString()
    {
        return "En:"+getEn()+" Boy:"+getBoy()+" Alan:"+alanHesapla();
    }
    
}

