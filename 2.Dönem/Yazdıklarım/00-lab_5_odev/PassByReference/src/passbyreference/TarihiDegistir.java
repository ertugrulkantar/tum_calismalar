/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package passbyreference;

/**
 *
 * @author ahmet
 */
public class TarihiDegistir {
    private int gun;
    private String ay;
    private int yil;
    
    public TarihiDegistir(int gun,String ay,int yil)
    {
        this.gun=gun;
        this.ay=ay;
        this.yil=yil;
    }
    
    public String toString()
    {
        return(gun+" "+ay+" "+yil);
    }
    
    public void HadiDegistir(TarihiDegistir birTarih)
    {
       birTarih.gun=this.gun;
       birTarih.ay=this.ay;
       birTarih.yil=this.yil;
       System.out.println("Metot icindeyken tarihimiz::"+birTarih);
       
    }
}

