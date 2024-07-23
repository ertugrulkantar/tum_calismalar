
package citymain;


public class CityMain {

   
    public static void main(String[] args) {
        
        City[] sehirler=new City[5];
        
        sehirler[0]=new City("Ankara",20);
        sehirler[1]=new City("Izmir",30);
        sehirler[2]=new City("Kars",5);
        sehirler[3]=new City("Istanbul",22);
        sehirler[4]=new City("Erzurum",3);
        
        System.out.println("Siralamadan Once\n------------------");
        for (City s : sehirler)
            System.out.println(s);
        
        GeneralizedSelectionSort.sort(sehirler,sehirler.length);
        System.out.println("\nSiralamadan Sonra\n------------------");
        for (City s : sehirler)
            System.out.println(s);
    }
    
    
}
