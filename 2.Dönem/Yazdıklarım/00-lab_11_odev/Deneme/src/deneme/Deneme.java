
package deneme;


public class Deneme {

    
    public static void main(String[] args) {
        
        Queue theQueue=new Queue(5);
        
        theQueue.insert(10);
        theQueue.insert(20);
        theQueue.insert(30);
        theQueue.insert(40);
        
        System.out.println(theQueue.remove());
        System.out.println(theQueue.remove());
        System.out.println(theQueue.remove());
        
        theQueue.insert(50);
        theQueue.insert(60);
        theQueue.insert(70);
        theQueue.insert(80);
        
        System.out.println("\nListenin son hali");
        System.out.println("-----------------");
        for (Object el:theQueue.kuyrukDizi)
            System.out.println(el);
        
        System.out.println();
        
        Customer customer1=new Customer("Ali Tuz","Bornova");
        Customer customer2=new Customer("Veli Demir","Alsancak");
        Customer customer3=new Customer("Can Ak","Cesme");
        
        Queue secondQueue=new Queue(4);
        
        secondQueue.insert(customer1);
        secondQueue.insert(customer2);
        secondQueue.insert(customer3);
        
        System.out.println(secondQueue.remove());
        System.out.println(secondQueue.remove());
        
        Customer customer4=new Customer("Cem Demir","Konak");
        Customer customer5=new Customer("Ayse Tuz","Bornova");
        Customer customer6=new Customer("Zeynep Karaca","Buca");
        
        secondQueue.insert(customer4);
        secondQueue.insert(customer5);
        secondQueue.insert(customer6);
        
        System.out.println("\nListenin son hali");
        System.out.println("-----------------");
        for (Object el:secondQueue.kuyrukDizi)
            System.out.println(el);
    }
    
}
