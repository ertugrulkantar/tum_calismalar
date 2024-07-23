package pkg5.lab_4_uygulamalar;


public class Lab_4_uygulamalar {

    public static void main(String[] args) {
        Nokta n1=new Nokta(3,4);
        Nokta n2=new Nokta(3,4);
        Nokta n3=new Nokta(6,8);
        
        System.out.println("n1 equals n2:"+n1.equals(n2));
        System.out.println("n1 equals n3:"+n1.equals(n3));
        
        Daire d1=new Daire(10, n1);
        Daire d2=new Daire(15, n3);
        Daire d3=new Daire(10, n1);
        
        System.out.println("d1 equals d2:"+d1.equals(d2));
        System.out.println("d1 equals d3:"+d1.equals(d3));
        
        System.out.printf("d1 çevre hesaplama:%6.2f\n",d1.cevreHesapla());
        System.out.printf("d1 alan hesaplama:%6.2f\n",d1.alanHesapla());
        System.out.printf("d2 çevre hesaplama:%6.2f\n",d2.cevreHesapla());
        System.out.printf("d2 alan hesaplama:%6.2f\n",d2.alanHesapla());
        System.out.printf("d3 çevre hesaplama:%6.2f\n",d3.cevreHesapla());
        System.out.printf("d3 alan hesaplama:%6.2f\n",d3.alanHesapla());
        
    }   
    
    
    
}
