
package hafta.pkg2;


public class Hafta2 {

   
    public static void main(String[] args) {
    
    /*if-else yazımı*/
    if (4>3)
        {
        System.out.println("Merhaba");
        }
    else{
        System.out.println("GG");
        }
    
    /*switch-case kavramları*/
    int n=2;
    switch (n)
        {
        case 1:
           System.out.println("qasdasd");
           break;
        case 2:
            System.out.println("adsasda");
            break;
        case 3:
            System.out.println("Buraya gir");
            break;
        default:
            System.out.println("Default");
            break;
        }
    
    /*if-else kısa ve farklı bir yol*/
    int n1=30;
    int n2=40;
    int max=(n1>n2)? n1:n2; //n1>n2 ise max'a 1.durumu(n1)ata.Değilse 2.durumu(n2)ata.
    System.out.println("Max="+max);
    
    // '==' Stringlerde eş adreslemeyi kontrol eder.
    // String karşılaştırmak için equals metodunu kullan.
    String s1="Hello World";
    String s2="hello world";
    String s3="Merhaba dunya";
    boolean k1=s1.equals(s3);   //İkisi aynı mı kontrol eder.
    System.out.println(k1);     //Boolean değişkene atanabilir.
    int strkarsilastir=s1.compareToIgnoreCase(s2);  //Büyük-küçük harfi yoksayarak
    System.out.println("Aynıysa:"+strkarsilastir);      //sözlük sıralaması yapar.
    int strkarsilastir2=s1.compareToIgnoreCase(s3);     //s1 önce geliyorsa negatif,
    System.out.println("1 once geliyorsa"+strkarsilastir2);     //s2 önce geliyorsa pozitif döndürür.
    
    /*Birleşik önermelerde 3 karşılaştırma yapılamaz; && ile 2'li 2'li bağlanır.*/
    if (1<2 && 2<3)
        {
            System.out.println("Dogru yaptın!");
        }    
    
    /*do-while kalıbı*/
    int while_kontrol=1;
    do
        {
            System.out.println(while_kontrol+".donus");   
        while_kontrol++;
        }while(while_kontrol<6);
        
    /*for loop*/
    for(int number=10;number!=10;number++)
        {
            System.out.println(number+".donus");
        }
                            
            
        
    }
    
    
}
