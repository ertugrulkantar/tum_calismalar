
package pkgfinal;
import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;


public class FinalMain {

    
    public static void main(String[] args) {
        
        DLL.head=null;  //Doublylinkedlist için
        DLL.tail=null;  //head ve tail ayarlandı.
        
        
        Vehicle[] aracDizi=new Vehicle[100];    //100'lük Vehicle array oluşturuldu.
        Scanner fileText1=null;         //fileText1, veriler.txt'yi almak için oluşturuldu.
        try{
            fileText1=new Scanner(new FileInputStream("veriler.txt"));} //veriler.txt, fileText1'e aktarıldı.
        
        catch (FileNotFoundException e){    //Exception handler.
            System.out.println("Dosya bulunamadi!!!");
            System.exit(0);}
        
        int i=-1;   //fileText1, aracDizi'ye işlenirken index 'i' ile ayarlanacak.
                    //İlk index 0 olduğundan ve en başta arttırma yapılacağından, ilk değer -1 olarak ayarlandı.
        
        while (fileText1.hasNext()) //Okunacak veri olduğu sürece döngü devam eder.
        {
            i=i+1;      
            String aracTuru=fileText1.next();   //Araç türü alındı.
            if(aracTuru.compareTo("car")==0)
            {   //Alttaki satır uzun görünüyor ancak bu şekilde kod ciddi manada kısalıyor.
            aracDizi[i]=new Car(fileText1.next(),fileText1.next(),fileText1.next(),Integer.valueOf(fileText1.next()));   
            }   //Car nesnesi olduğu belirlendikten sonra fileText1'in sıradaki içeriği Car'ın parametrelerine göre uygun şekilde yerleştirildi.
            else
            {
            aracDizi[i]=new Truck(fileText1.next(),fileText1.next(),fileText1.next(),Integer.valueOf(fileText1.next()));   
            }        //Aynı mantık Truck nesneleri için de uygulandı.
                
            
        }
        
        System.out.println("Vehicle dizisi yazdırılıyor!\n>>>========================<<<");
        for (Vehicle eleman:aracDizi)
        {
            if(eleman!=null)    //null olan elemanları ayıkladık.
            {   
                System.out.println(eleman); //İlk önce eldeki eleman yazdırılıyor.
                if(eleman instanceof Car)   //Sınıf Car ise araba türü de yazdırılacağından burada
                {                           //kapı sayısına göre yazdırılacaklar ayarlandı.
                    if(((Car) eleman).getKapiSayisi()==4)
                        System.out.println("***Normal araba***");
                     
                    else if(((Car) eleman).getKapiSayisi()==5)  
                    {
                        System.out.println("***SWagon araba***");
                    }   
                    
                    else
                        System.out.println("***Spor araba***"); //İkisi de değilse spor arabadır.
                }   
            System.out.println("-----------------------------");            
            }               
        }        
       
        System.out.println("!!!Vehicle dizisi yazdırıldı!!!\n");
       
       for(Vehicle eleman:aracDizi) //Dizi içindeki elemanlar çift bağlı listeye işleniyor.
       {
           if(eleman!=null)
           {
               DLL.siraliEkle(eleman);
           }
       }
       System.out.println("Cift bagli liste yazdiriliyor!\n>>>========================<<<");
       DLL.ondenYazdir();   //Burada baştan mı sondan mı yazdırılacağı detay olarak verilmemiş, baştan yazdırıldı.
       System.out.println("!!!Cift bagli liste yazdırıldı!!!\n");
       
       
        Scanner fileText2=null;     //islemler.txt, fileText2'ye aktarıldı.
        try{
            fileText2=new Scanner(new FileInputStream("islemler.txt"));}
        
        catch (FileNotFoundException e){    //Exception handler.
            System.out.println("Dosya bulunamadi!!!");
            System.exit(0);}
    
        
        while (fileText2.hasNext())   //Okunacak veri olduğu sürece döngü devam eder.
        {
            String komut=fileText2.next();  //Komut alındı.
            if(komut.compareTo("ekle")==0)  
            {
                String aracTuru=fileText2.next();
                if(aracTuru.compareTo("car")==0)
                {
                    Car c=new Car(fileText2.next(),fileText2.next(),fileText2.next(),Integer.valueOf(fileText2.next()));
                    DLL.siraliEkle(c);  //Üstteki satır yine uzun görünüyor ancak kodu kısaltıyor.
                }                       //İşleyişi bu şekilde daha iyi görebiliyorum.
                else    //Eğer sınıf Car değilse Truck'tır.
                {
                    Truck t=new Truck(fileText2.next(),fileText2.next(),fileText2.next(),Integer.valueOf(fileText2.next()));
                    DLL.siraliEkle(t);  
                }
            }       
            else
            {
                String silinecekPlaka=fileText2.next(); //Eğer komut ekle değilse sil komutudur.
                DLL.plakaylaSil(silinecekPlaka);        //Dolayısıyla sıradaki String'i okuyup metoda veriyoruz.
            }
        }
        
        System.out.println("'islemler.txt' uygulandıktan sonra liste bastan yazdiriliyor!\n>>>========================<<<");
        DLL.ondenYazdir();
        System.out.println("!!!Liste bastan yazdırıldı!!!\n");
        
        System.out.println("'islemler.txt' uygulandıktan sonra liste sondan yazdiriliyor!\n>>>========================<<<");
        DLL.sondanYazdir();
        System.out.println("!!!Liste sondan yazdırıldı!!!");
}       

}
