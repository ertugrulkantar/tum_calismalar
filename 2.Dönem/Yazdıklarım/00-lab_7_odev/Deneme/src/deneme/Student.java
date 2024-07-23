
package deneme;


public class Student extends Person {
    
    private String ID;
    private int seviye;

    
    public String getID() {
        return ID;
    }


    public void setID(String ID) {
        this.ID = ID;
    }

    
    public int getSeviye() {
        return seviye;
    }

  
    public void setSeviye(int seviye) {
        this.seviye = seviye;
    }

    public Student()    //Parametresiz constructor.
    {
        super();
        ID="Mevcut degil!";
        seviye=0;
    }

    public Student(String ad,String soyad,String ID,int seviye) //Tüm parametrelere sahip constructor.
    {
        super(ad,soyad);
        
        if(ID==null || seviye==0)
        {
            System.out.println("Student olusturmada hata!");
            System.exit(0);
        }
        this.ID=ID;
        this.seviye=seviye;
    }
    
    public Student(Student orjinalStudent)
    {
        super(orjinalStudent.getAd(),orjinalStudent.getSoyad());
        ID=orjinalStudent.getID();
        seviye=orjinalStudent.getSeviye();
    }
    
    public String toString()
    {
        String pre=super.toString();
        return(pre+" ID::"+getID()+" Seviye::"+getSeviye());
    }
    
    public boolean equals(Object digerObje)
    {
        if (digerObje==null)
            return false;
        else if (this.getClass()!=digerObje.getClass())
            return false;
        else
        {
            Student digerogrenci=(Student) digerObje;
            return (this.getAd().equals(digerogrenci.getAd())) &&
                    (this.getSoyad().equals(digerogrenci.getSoyad())) &&
                    (this.getID().equals(digerogrenci.getID())) &&
                    (this.getSeviye()==(digerogrenci.getSeviye()));
                   
        }
    }
    
}
