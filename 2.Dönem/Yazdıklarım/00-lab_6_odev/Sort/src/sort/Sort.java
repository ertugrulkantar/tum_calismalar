
package sort;

public class Sort {

 
    public static void main(String[] args) {
        
       int dizi1[]={99,3,35,52,88,13};   //Sırasız bir dizi oluşturup
       InsertionSort.sirala(dizi1);      //statik metoda argüman olarak verdim.
       System.out.println("Dizinin sirali hali::");
       for (int eleman: dizi1)           //for-each loop ile printliyorum.
       {
           System.out.print(eleman+" ");
       }
    }
    
}
